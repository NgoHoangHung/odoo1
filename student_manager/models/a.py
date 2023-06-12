
from odoo import models, fields, api


class A(models.Model):
   _name = 'a'
   
   name = fields.Char("amodel",require = True)
   age = fields.Integer()
   rel_test3 = fields.Many2one('test3',string = "test",ondelete = 'cascade')
   