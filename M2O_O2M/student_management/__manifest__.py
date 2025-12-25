{
    'name': 'Student Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage students and courses',
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',
    'views/student_view.xml',
    'views/course_view.xml',
    'views/menu.xml',
    ],

    'installable': True,
    'application': True,
}
