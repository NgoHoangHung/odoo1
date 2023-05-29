from odoo import api, fields,models

class AkioEmployee(models.Model):
    _name = 'akio.employee'
    _parent_name = "parent_id"
    _inherit = 'akio.customer'
    
    name = fields.Char(string = "Employee")
    parent_id = fields.Many2one('akio.employee', 'Manager',ondelete = 'cascade')
    child_id = fields.One2many('akio.employee','parent_id','Child Employee')
    job = fields.Char("Work")
    experience = fields.Integer('Experience')
    