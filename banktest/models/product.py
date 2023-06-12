from odoo import models, fields, api, exceptions
from datetime import datetime


# from datetime
class Product(models.Model):
    _name = 'product'

    def get_default_purchase_date(self):
        return datetime.now()

    name = fields.Char(string="Product Name", required=True, index='trigram')
    price = fields.Integer(string="Price")
    purchase_date = fields.Datetime(
        string="Purchase Date", default=get_default_purchase_date)
    warranty = fields.Selection(selection=[('warranty', 'Warranty'), ('not', 'Not Warranty')],
                                string='Warranty')
    vat = fields.Float(default=0.1, string='VAT')
    revenue = fields.Float(compute='_onchange_price')
    price_with_tax = fields.Float(string='Price Tax', compute="get_price_with_tax")#, store=True
    amount = fields.Integer(string='amount')
    active = fields.Boolean(string='Active', default=True)
    supplier_ids = fields.Many2many(comodel_name='supplier', relation='supplier_product_rel',
                                    column1='product_id', column2='supplier_id', string='Supplier')
    category_id = fields.Many2one(comodel_name='category', string='Category')

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Product name must be unique!'),
        ('price_pos', 'CHECK(price >=0)', 'Product price must be positive!')
    ]

    @api.depends('price', 'vat')
    # @api.depends()
    def get_price_with_tax(self):
        for product in self:
            if product.price:
                product.price_with_tax = product.price + product.price * product.vat
            else:
                product.price_with_tax = product.price

    # @autovacuum
    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Product, self).create(vals)
        return record

    def write(self, vals):
        result = super(Product, self).write(vals)
        return result

    def unlink(self):
        return super(Product, self).unlink()

    @api.onchange('price')
    def onchange_price(self):
        if self.price and self.price < 5:
            self.warranty = 'not'
        else:
            self.warranty = 'warranty'

    @api.onchange('amount', 'price')
    def _onchange_price(self):
        self.revenue = self.amount * self.price
        # return {
        #     'warning': {
        #         'title': 'sthing1',
        #         'message': 'sthing2'
        #     }
        # }

    @api.constrains('price')
    def validate_price(self):
        if self.price < 0:
            raise exceptions.ValidationError('Price need greater than 0')
