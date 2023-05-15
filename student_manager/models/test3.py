from odoo import models, fields, api


class Test3(models.Model):
    _name = 'test3'
    # _log_access = True
    # _transient = True
    # _check_company_auto= True
    # _sequence
    # _parent_store = True

    # parent_path = fields.Char(required=True)

    name = fields.Char('Name')
    number = fields.Integer('Number')
    #
    # state = fields.Selection(string='Status', selection=[('new', 'New'),
    #                                                     ('studying', 'Studying'),
    #                                                     ('off', 'Off')],
    #                                                 default='new')
    # test2_id = fields.Many2one('test2', string='Level',
    #                                    states={'new': [('invisible', True),('readonly', True)],
    #                                            'studying': [('invisible', False),('readonly', True)],
    #                                            'off': [('invisible', True),('readonly', True)]})
    
