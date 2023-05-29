from odoo import api, fields, models


class AkioPartner(models.Model):
    _inherit = "res.partner"
    
    def akio_debug(self):
        pass
    
    
    @api.model
    def create(self, vals):
        print("______________________________________________________________________")
        print("Env: ", self.env)
        print("______________________________________________________________________")
        print("User: ", self.env.user)
        print("______________________________________________________________________")
        print("company: ", self.env.company)
        print("______________________________________________________________________")
        print("Companies: ", self.env.companies)
        print("______________________________________________________________________")
        print("Context: ", self.env.context)
        print("______________________________________________________________________") 
        
        pass
        print("partner values",vals)
        return super(AkioPartner,self).create(vals)