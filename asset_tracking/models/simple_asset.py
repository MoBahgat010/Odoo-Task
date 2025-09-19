from odoo import api, fields, models

class SimpleAsset(models.Model):
    _name = 'simple.asset'
    _description = 'Simple Asset'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    barcode = fields.Char(string='Barcode', readonly=True)
    serial_number = fields.Char(string='Serial Number')
    employee_id = fields.Many2one('hr.employee', string='Assigned To', tracking=True)
    transfer_ids = fields.One2many('simple.asset.transfer', 'asset_id', string='Transfer History')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('barcode'):
                vals['barcode'] = self.env['ir.sequence'].next_by_code('simple.asset.barcode')
        return super().create(vals_list)

class SimpleAssetTransfer(models.Model):
    _name = 'simple.asset.transfer'
    _description = 'Asset Transfer History'

    asset_id = fields.Many2one('simple.asset', required=True, ondelete='cascade')
    from_employee_id = fields.Many2one('hr.employee', string='From Employee')
    to_employee_id = fields.Many2one('hr.employee', string='To Employee', required=True)
    date = fields.Date(string='Transfer Date', required=True)