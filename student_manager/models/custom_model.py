from odoo import models, fields, api

class Mixinclass(models.AbstractModel):
    _name = 'company.mixin.class'
    
    code = fields.Char(string="code",invisible = True)
    verified= fields.Boolean(string = 'Verifired')
    data = fields.Date(string ="Date",default = fields.Date.today())
    name= fields.Char(string="Name")
    
class CustomModel(models.Model):
    _name = 'custom.model'
    _inherit = ['company.mixin.class']


