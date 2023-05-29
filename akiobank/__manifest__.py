{
    'name': "Ngân Hàng ABC",# -*- coding: utf-8 -*-
    'version': '1.0',
    'summary': 'Odoo Learn ',
    'sequence': 1,
    'author': 'Akio',
    'description': """
    module cho mọi nhà
    """,
    'category': 'Orther',
    'website': '',
    'depends': [],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        
        'wizard/akio_transaction_view.xml',
        'wizard/akio_withdraw_money_view.xml',
        'wizard/akio_charge_money_view.xml',
        
        'views/akio_customer_view.xml',
        'views/akio_wallet_view.xml',
        'views/akio_trans_history_view.xml',
        'views/akio_schedule_view.xml',

        'views/akio_customer_view_inherit.xml',
        'views/akio_employee_view.xml',
        
        'views/mybank_menus.xml',
    ],
    'installable': True,
    'application': True,
}