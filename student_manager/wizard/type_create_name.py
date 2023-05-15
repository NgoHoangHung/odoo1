from odoo import api, fields, models


class TypeCreateName(models.TransientModel):
    _name = 'type.create.name'

    name = fields.Char(string='Name')

    @api.model
    def create_name(self,name):
        # print('hung')
        class_no = self.env['class.no']
        class_no.super(TypeCreateName,self).create_name(name)
