{
    'name': "Hỗ trợ tài chính",# -*- coding: utf-8 -*-
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
        'wizard/akio_sendmoney_view.xml',
        
        'views/akio_customer_view.xml',
        'views/akio_wallet_view.xml',
        'views/akio_trans_history_view.xml',

        'views/mybank_menus.xml',
    ],
    'installable': True,
    'application': True,
}