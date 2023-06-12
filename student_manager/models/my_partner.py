from odoo import models, fields, api

class My_Partner(models.Model):
    _inherit= 'res.partner'
    
    @api.model
    def create(self,vals):
        print("User Env",self.env)
        print("User Env",self.env.user)
        print("User Env",self.env.company)
        print("User Env",self.envcompanies)
        print("User Env",self.env.context)

        print ('partner value',vals)