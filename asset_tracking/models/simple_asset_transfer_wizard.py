from odoo import fields, models

class SimpleAssetTransferWizard(models.TransientModel):
    _name = 'simple.asset.transfer.wizard'
    _description = 'Asset Transfer Wizard'

    asset_id = fields.Many2one('simple.asset', required=True)
    to_employee_id = fields.Many2one('hr.employee', string='Transfer To', required=True)
    date = fields.Date(string='Date', default=fields.Date.context_today, required=True)

    def action_transfer(self):
        self.ensure_one()
        self.asset_id.message_post(body=f"Asset transferred from {self.asset_id.employee_id.name or 'Unassigned'} to {self.to_employee_id.name} on {self.date}.")
        self.env['simple.asset.transfer'].create({
            'asset_id': self.asset_id.id,
            'from_employee_id': self.asset_id.employee_id.id,
            'to_employee_id': self.to_employee_id.id,
            'date': self.date,
        })
        self.asset_id.employee_id = self.to_employee_id
        return {'type': 'ir.actions.act_window_close'}