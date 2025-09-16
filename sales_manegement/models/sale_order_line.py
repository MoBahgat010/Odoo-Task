# custom_sales_attributes/models/sale_order_line.py
from odoo import models, api, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    department_id = fields.Many2one(
        'sales.department',
        string='Department',
        help='Department for this order line',
        related='order_id.department_id',
        store=True,
        readonly=False
    )

    @api.onchange('product_id', 'product_uom_qty')
    def _onchange_product_attributes(self):
        """Recalculate price and amount when product or quantity changes."""
        if self.product_id:
            self._compute_price_unit()
            if hasattr(self, 'amount'):
                self.amount = self.product_uom_qty * self.price_unit
            self._onchange_discount()

    @api.model_create_multi
    def create(self, vals_list):
        """Set department from order when creating new line"""
        lines = super().create(vals_list)
        for line in lines:
            if line.order_id.department_id and not line.department_id:
                line.department_id = line.order_id.department_id.id
        return lines