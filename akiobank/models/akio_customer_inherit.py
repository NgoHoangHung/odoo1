from odoo import api,models,fields

class AkioCustomerInherit(models.Model):
    _inherit ='akio.customer'
    
    # name = fields.Char(string = "Siêu Khách Hàng")
    local = fields.Char(string = "Khu Vực",default = 'Asean')
    