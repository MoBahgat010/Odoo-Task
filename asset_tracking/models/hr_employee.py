from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    asset_ids = fields.One2many('simple.asset', 'employee_id', string='Assigned Assets')