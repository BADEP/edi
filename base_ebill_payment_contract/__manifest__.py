# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Base eBill Payment Contract",
    "summary": "Base for managing e-billing contracts",
    "version": "20.0.1.0.0",
    "development_status": "Beta",
    "license": "AGPL-3",
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "maintainers": ["TDu"],
    "website": "https://github.com/OCA/edi",
    "depends": ["account_invoice_transmit_method"],
    "data": [ "views/ebill_payment_contract.xml", 'security/ir.access.csv'],
    "demo": ["demo/ebill_payment_contract.xml"],
}
