# custom_invoice_attributes/models/account_move_line.py
from odoo import models, api, fields

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    department_id = fields.Many2one(
        'sales.department',
        string='Department',
        help='Department for this invoice line',
        related='move_id.department_id',
        store=True,
        readonly=False
    )

    @api.onchange('product_id', 'quantity')
    def _onchange_product_attributes(self):
        """Recalculate price and amount when product or quantity changes."""
        if self.product_id:
            self._compute_amount()
            if hasattr(self, 'price_subtotal'):
                self.price_subtotal = self.quantity * self.price_unit
            self._onchange_discount()

    @api.model_create_multi
    def create(self, vals_list):
        """Set department from move when creating new line"""
        lines = super().create(vals_list)
        for line in lines:
            if line.move_id.department_id and not line.department_id:
                line.department_id = line.move_id.department_id.id
        return lines