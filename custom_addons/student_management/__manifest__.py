{
    'name': 'Student Management',
    'version': '1.0',
    'category': 'Education',
    'depends': ['base', 'mail'],  # mail needed for chatter
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
    ],
    'application': True,
    'installable': True,
}
