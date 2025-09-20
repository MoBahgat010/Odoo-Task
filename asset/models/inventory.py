# models/inventory.py
from odoo import api, fields, models

class AssetInventory(models.Model):
    _name = 'asset.inventory'
    _description = 'Asset Inventory'

    name = fields.Char(string='Inventory Name', required=True)
    line_ids = fields.One2many('asset.inventory.line', 'inventory_id', string='Lines')
    scan_barcode = fields.Char(string='Scan Barcode')

    @api.onchange('scan_barcode')
    def _onchange_scan_barcode(self):
        if self.scan_barcode:
            asset = self.env['custom.asset'].search([('asset_id', '=', self.scan_barcode)], limit=1)
            if asset:
                new_line = {'asset_id': asset.id}
                self.line_ids = [(0, 0, new_line)]
            self.scan_barcode = False

class AssetInventoryLine(models.Model):
    _name = 'asset.inventory.line'
    _description = 'Asset Inventory Line'

    inventory_id = fields.Many2one('asset.inventory', string='Inventory', required=True, ondelete='cascade')
    asset_id = fields.Many2one('custom.asset', string='Asset', required=True)