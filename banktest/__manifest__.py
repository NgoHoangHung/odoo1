{
    'name': "Bank Test",# -*- coding: utf-8 -*-
    'version': '1.0',
    'summary': 'Odoo Learn ',
    'sequence': 1,
    'author': 'Akio',
    'description': """
    learn odoo
    """,
    'category': 'Orther',
    'website': '',
    # 'depends': ['purchase'],
    'data': [
        'wizard/employee_leave_reason_view.xml',
        
        'views/product_view.xml',
        'views/supplier_view.xml',
        'views/category_view.xml',
        'views/employee_view.xml',
        
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}