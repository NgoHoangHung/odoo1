from odoo import models,fields
class Partner(models.Model):
    _inherit = 'res.partner'
    
    hotline = fields.Char(string = 'Hotline')