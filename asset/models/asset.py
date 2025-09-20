# models/asset.py
from odoo import fields, models

class Asset(models.Model):
    _name = 'custom.asset'
    _description = 'Asset'

    name = fields.Char(string='Name', required=True)
    asset_id = fields.Char(string='Asset ID', required=True, index=True)
    
    _sql_constraints = [
        ('asset_id_unique', 'unique(asset_id)', 'Asset ID must be unique.')
    ]