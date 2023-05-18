from odoo import api, fields, models


class Wallet(models.Model):
    _name = "wallet"
    _rec_name = 'akio_customer_id'

    accountnumber = fields.Char(
        string="Số Tài Khoản", compute='accountnumber_gen',store=True) 
    password = fields.Char(string="Mật Khẩu",)
    balance = fields.Float(string="Số Dư")
    bank_name = fields.Selection([('bidv', 'BIDV'),
                                 ('vtb', 'Viettin Bank'),
                                 ('acb', 'Á Châu Bank'),
                                 ('tech', 'Techcom Bank')
                                  ], string="Ngân Hàng")

    akio_customer_id = fields.Many2one(comodel_name="akio.customer",
                                       string="Khách Hàng")

    transaction_history_ids = fields.One2many('trans.history', inverse_name="wallet_id", string = "Lịch sử giao dịch")
    
    akio_schedule_ids = fields.One2many(
        comodel_name = 'akio.schedule',
        inverse_name = 'wallet_id',
        string = "Schedule"
        )

    @api.depends('bank_name', 'akio_customer_id.phone')
    def accountnumber_gen(self):
        for record in self:
            self.accountnumber = str(self.bank_name) + str(self.akio_customer_id.phone)
    
    def is_cal(self):
        return True if self.balance > 0 else False
    
   