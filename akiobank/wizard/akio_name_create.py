from odoo import fields,models,api
class AkioNameCreate(models.Transient):
    _name = 'akio.name.create'
    
    name = fields.Char("Khách Hàng")
    
    
    def name_create(self,name):
        new_customer = self.env['akio.customer']
        record={
            'name': self.name
            }
        