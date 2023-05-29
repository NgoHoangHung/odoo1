from odoo import fields, models, api


class AkioTransaction(models.TransientModel):
    _name = 'akio.transaction'

    deposit = fields.Float("Số Tiền")
    customer_receive = fields.Many2one(comodel_name="akio.customer",
                                       string="Người Nhận")
    account_number = fields.Many2one('wallet', string="Số Tài Khoản Nhận")
    content_trans = fields.Text("Nội Dung Giao Dịch")
    

    
    def sendmoney(self):
        receiver_wallet = self.account_number
        sender_wallet = self.env['wallet'].search([('akio_customer_id.id', '=', self._context.get('active_id'))])
        
        receiver_wallet.balance = receiver_wallet.balance + self.deposit
        sender_wallet.balance = sender_wallet.balance - self.deposit
        receiver_history={
            'trans_type':'1',
            'deposit':  self.deposit,
            'creat_at': fields.Datetime.now(),
            'partner_id': sender_wallet.akio_customer_id.name,
            'content_trans': self.content_trans
        }
        receiver_wallet.write({
         'transaction_history_ids':[(0,0,receiver_history)] 
        })
        
        sender_history={
            'trans_type':'0',
            'deposit':  self.deposit,
            'creat_at': fields.Datetime.now(),
            'partner_id': receiver_wallet.akio_customer_id.name,
            'content_trans': self.content_trans
        }
        sender_wallet.write({
         'transaction_history_ids':[(0,0,sender_history)] 
        })

    def charge_money(self):
        charger_wallet = self.env['wallet'].search([('akio_customer_id.id', '=', self._context.get('active_id'))])
        charger_wallet.balance = charger_wallet.balance + self.deposit
        
        charge_history={
            'trans_type':'3',
            'deposit':  self.deposit,
            'creat_at': fields.Datetime.now(),
            # 'partner_id': sender_wallet.akio_customer_id.name,
            # 'content_trans': self.content_trans
        }
        charger_wallet.write({
         'transaction_history_ids':[(0,0,charge_history)] 
        })
        
    def withdraw_money(self):
        withdrawer_wallet = self.env['wallet'].search([('akio_customer_id.id', '=', self._context.get('active_id'))])
        withdrawer_wallet.balance = withdrawer_wallet.balance - self.deposit
        
        withdraw_history={
            'trans_type':'2',
            'deposit':  self.deposit,
            'creat_at': fields.Datetime.now(),
            # 'partner_id': sender_wallet.akio_customer_id.name,
            # 'content_trans': self.content_trans
        }
        withdrawer_wallet.write({
         'transaction_history_ids':[(0,0,withdraw_history)] 
        })
        
    @api.onchange('account_number')
    def _onchange_account_number(self):
        if self.account_number:
            self.customer_receive = self.account_number.akio_customer_id
            
