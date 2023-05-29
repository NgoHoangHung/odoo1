from odoo import models, fields, api


class C(models.Model):
    _name = 'c'
    _inherits = {'b': 'b_id',
        'test2': 'test2_id'}

    name = fields.Char(string = "Profile")
    # maker = fields.Char(string='Maker')

    b_id = fields.Many2one('b', required=True, ondelete="cascade")
    test2_id = fields.Many2one('test2', required=True, ondelete="cascade")