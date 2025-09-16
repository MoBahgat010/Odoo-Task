{
    'name': 'Custom Sales Attributes',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Customize sales order lines for immediate attribute updates',
    'depends': ['sale', 'hr'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
}