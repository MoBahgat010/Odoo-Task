{
    'name': 'WhatsApp Integration for Contacts',
    'version': '18.0.1.0.0',
    'summary': 'Add WhatsApp chat button',
    'website': 'https://yourwebsite.com',
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/partner_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}