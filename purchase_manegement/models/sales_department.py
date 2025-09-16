from odoo import models, fields

class SalesDepartment(models.Model):
    _name = 'sales.department'
    _description = 'Sales Department'

    name = fields.Char(string="Department Name", required=True)