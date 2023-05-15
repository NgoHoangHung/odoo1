from odoo import models, fields
class Mixinclass(models.AbstractModel):
    _name = 'company.minxin.class'
    
    code = fields.Char(string="code",invisible = True)
    verified= fields.Boolean(string = 'Verifired')
    data = fields.Date(string ="Date",default = fields.Date.today())
    name= fields.Char(string="Name")