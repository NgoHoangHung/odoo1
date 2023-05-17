from odoo import fields, models, api


class Category(models.Model):
    _name = 'category'

    name = fields.Char(string='Category')
    description = fields.Char(string="Description")
    product_ids = fields.One2many(
        comodel_name='product', inverse_name='category_id', string='Product')
    product_count = fields.Integer(
        compute='get_product_count', string='Product Count', store=True)

    @api.depends('product_ids')
    def get_product_count(self):
        for cate in self:
            cate.product_count = len(cate.product_ids)

    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Category, self).create(vals)
        return record

    def write(self, vals):
        return super(Category, self).create(vals)

    def unlink(self):
        return super(Category, self).unlink()

    def action_product(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('List Product'),
            'res_model': 'product',
            'view_type': 'form',
            'view_mode': 'list,form',
            'domain': [('category_id', '=', self.id)],
        }
