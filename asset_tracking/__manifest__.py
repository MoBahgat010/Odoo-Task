{
    'name': 'Asset Tracking',
    'version': '1.0',
    'depends': ['base', 'hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequences.xml',
        'views/simple_asset_views.xml',
        'views/hr_employee_views.xml',
        'views/asset_transfer_wizard_views.xml',
    ],
    'installable': True,
    'application': True,
}