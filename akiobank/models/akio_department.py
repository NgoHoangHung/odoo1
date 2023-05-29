from odoo import api, fields, models

class AkioDepartment(models.Model):
    _name = 'akio.department'
    
    name = fields.Char(string = 'Phòng')