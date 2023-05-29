from odoo import models, fields, api


class Test3(models.Model):
    _name = 'test3'
    # _log_access = True
    # _transient = True
    # _check_company_auto= True
    # _sequence
    # _parent_store = True

    # parent_path = fields.Char(required=True)

    name = fields.Char('Name')
    origin_price = fields.Float('Giá Gốc')
    # profit_rate= fields.Float('Tỉ Lệ Lãi')
    discount = fields.Float('Giảm Giá')
    sale_price = fields.Float('Giá Bán', compute="_sale_price", inverse="_recompute_price", store=True, readonly=False)
    # sale_discount= fields.Float('Giá Còn')
    
    def _recompute_price(self):
        for i in self: 
            i.origin_price = i.sale_price / (1- i.discount)
    
    @api.depends('origin_price', 'discount')
    def _sale_price(self):
        for i in self:
            i.sale_price = i.origin_price - i.origin_price * i.discount
    #===========================================================================
    #===========================================================================
    #===========================================================================
    # # # End
    #===========================================================================
    #===========================================================================
    #===========================================================================
