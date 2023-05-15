from odoo import models, fields, api


class Supplier(models.Model):
    _name = 'supplier'

    name = fields.Char(string="Provider")
    product_ids = fields.Many2many(comodel_name='product', relation='supplier_product_rel',
                                   column1='supplier_id', column2='product_id', string='Product')

    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Supplier, self).create(vals)
        return record

    def write(self, vals):
        result = super(Supplier, self).write(vals)
        return result

    def unlink(self):
        return super(Supplier, self).unlink()
