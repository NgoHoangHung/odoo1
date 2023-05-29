from odoo import models, fields, api


class B(models.Model):
    _name = 'b'
    _inherit = 'a'
    
    
    name = fields.Char("bhuhu",help= 'test')
    phone = fields.Char(string = "Phone")
    
        