from odoo import api, fields, models
from odoo.exceptions import ValidationError


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    previous_reading = fields.Float(
        string="Previous Reading",
        default=0.0,
    )

    new_reading = fields.Float(
        string="New Reading",
        default=0.0,
    )

    actual_reading = fields.Float(
        string="Actual Reading",
        compute="_compute_actual_reading",
        store=True,
        readonly=True,
    )

    # COMPUTE METHOD; For getting the actual reading
    @api.depends("previous_reading", "new_reading")
    def _compute_actual_reading(self):
        for line in self:
            line.actual_reading = line.new_reading - line.previous_reading


    @api.onchange("previous_reading", "new_reading")
    def _onchange_meter_readings(self):
        for line in self:
            line.quantity = line.new_reading - line.previous_reading

    @api.onchange("product_id", "move_id.partner_id")
    def _onchange_previous_reading(self):
        for line in self:

            line.previous_reading = 0.0

            partner = line.move_id.partner_id
            product = line.product_id

            if not partner or not product:
                continue

            previous_line = self.env["account.move.line"].search(
                [
                    ("move_id.partner_id", "=", partner.id),
                    ("move_id.state", "=", "posted"),
                    ("move_id.move_type", "=", "out_invoice"),
                    ("product_id", "=", product.id),
                ],
                order="id desc",
                limit=1,
            )

            if previous_line:
                line.previous_reading = previous_line.new_reading
                
                
    @api.constrains("previous_reading", "new_reading")
    def _check_meter_readings(self):
        for line in self:
            if line.new_reading < line.previous_reading:
                raise ValidationError(
                    "New Reading cannot be less than Previous Reading."
                )