# Meter Invoice Reading

## Meter Invoice Reading
This module adds meter-based invoicing support to Odoo by tracking meter readings on invoice lines and calculating actual consumption automatically.

## Requirements
- Odoo 19 Community
- PostgreSQL 16
- Standard Odoo invoicing and product setup

## Features
- Adds **Previous Reading** field to invoice lines
- Adds **New Reading** field to invoice lines
- Calculates **Actual Reading** (consumption) automatically
- Synchronizes invoice line **Quantity** with consumption
- Automatically retrieves the previous meter reading for the same product/customer
- Extends invoice PDF output to include meter reading details
- Validates readings to prevent negative consumption

## Installation
1. Copy the `meter_invoice` folder into your Odoo addons directory.
2. Restart the Odoo service.
3. Update the Apps list from the Apps menu.
4. Install **Meter Invoice Reading**.

## Testing
1. Create an initial invoice with a meter reading on the invoice line.
2. Post the invoice.
3. Create a second invoice for the same customer and product.
4. Confirm the **Previous Reading** is populated from the prior invoice's **New Reading**.
5. Verify that the calculated quantity matches the actual consumption and appears correctly on the invoice PDF.

## Notes
- Designed for Odoo 19 and PostgreSQL 16.
- Works with standard invoice workflows and printed PDF reports.