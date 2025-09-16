from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    department_id = fields.Many2one(
        'sales.department',
        string='Department',
        help='Department for this invoice or bill'
    )