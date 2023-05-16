from odoo import fields, models, api


class AkioTransaction(models.TransientModel):
    _name = 'akio.transaction'

    deposit = fields.Float("Số Tiền")
    customer_receive = fields.Many2one(comodel_name="akio.customer",
                                       string="Người Nhận")
    account_number = fields.Many2one('wallet', string="Số Tài Khoản")

    def sendmoney(self):
        receiver_wallet = self.env['wallet'].search(
            [('akio_customer_id.id', '=', self.customer_receive.id)])
        sender_wallet = self.env['wallet'].search(
            [('akio_customer_id.id', '=', self._context.get('active_id'))])
        receiver_wallet.balance = receiver_wallet.balance + self.deposit
        sender_wallet.balance = sender_wallet.balance - self.deposit

    @api.onchange('account_number')
    def _onchange_account_number(self):
        domain = {'customer_receive': [
            ('id', '=', self.account_number.akio_customer_id.id)]}
        return {'domain': domain}

    # bank_name = fields.Selection([('bidv', 'BIDV'),
    #                               ('vtb', 'Viettin Bank'),
    #                               ('acb', 'Á Châu Bank'),
    #                               ('tech', 'Techcom Bank')
    #                               ], string="Ngân Hàng")
