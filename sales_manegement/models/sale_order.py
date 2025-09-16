from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    department_id = fields.Many2one(
        'sales.department',
        string='Department',
        help='Department for this sales order'
    )