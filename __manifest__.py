
# -*- coding: utf-8 -*-biểu
{
    'name': "student_manager",
    'sequence': 2,
    'description': """
       Student Manager Soft for school
    """,
    'author': "Akio",
    'version': '0.1',
    'depends': ['base'],
    'data': [

        'views/course_view.xml',
        'views/student_detail_line_view.xml',
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/class_no_view.xml',
        'views/class_detail_view.xml',
        

        'security/security.xml',
        'security/ir.model.access.csv',

        'views/student_menus.xml',
    ],
    'installable': True,
    'application': True,
}
