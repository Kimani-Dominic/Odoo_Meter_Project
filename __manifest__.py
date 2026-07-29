{
    "name": "Meter Invoice Reading",
    "version": "1.0.0",
    "summary": "Adds meter readings to customer invoices",
    "category": "Accounting",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv"
        "views/account_move_views.xml",
        "reports/invoice_report.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
