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
    test_onchange = fields.Selection(selection = [
        ('0','Ok'),
        ('1','No Ok')
        ])
    test2_ids = fields.Many2many(
       comodel_name='test2',
       relation='test3_test2_rel',
       column1 = 'test3_id',
       column2='test2_id',
       string = 'Test2'
       )
    def _recompute_price(self):
        for i in self: 
            i.origin_price = i.sale_price / (1- i.discount)
    
    def test3_debug(self):
        pass
    
    @api.onchange('discount')
    def _onchange_discount(self):
        if self.discount <= 1:
            self.test_onchange = '0'
        elif self.discount >1:
            self.test_onchange = '1'
                
    
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
