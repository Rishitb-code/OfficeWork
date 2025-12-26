{
    'name': 'Training Management',
    'version': '1.0',
    'category': 'Training',
    'summary': 'Example module using Many2one, One2many and Many2many',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/training_views.xml',
        'views/training_menu.xml',
    ],
    'installable': True,
    'application': True,
}
