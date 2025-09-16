from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    department_id = fields.Many2one(
        'sales.department',
        string='Department',
        help='Department for this purchase order'
    )