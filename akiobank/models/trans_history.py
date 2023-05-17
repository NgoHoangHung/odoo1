from odoo import api, fields, models
from odoo import exceptions


class TransHistory(models.Model):
    _name = "trans.history"
    _discription = '''
    lịch sử
    '''
    _rec_name = 'wallet_id'
    # name = fields.Char(string="Lịch Sử Giao Dịch")
    trans_type = fields.Selection([
        ('0', 'Chuyển tiền'),
        ('1', 'Nhận tiền')
        #   ('2','Gửi Tiết Kiệm'),
        #   ('3','Thanh Toán Hóa Đơn')
    ], string="Loại Giao Dịch", default='0')
    deposit = fields.Float(string="Số Tiền")
    creat_at = fields.Datetime(
        string="Ngày giao dịch", default=lambda self: fields.Datetime.now())
    wallet_id = fields.Many2one("wallet", string="Ví")
    partner_id = fields.Char("Đối Tác")
    content_trans = fields.Text("Nội Dung Giao Dịch")

    @api.constrains('name', 'description')
    def _check_description(self):
        for record in self:
            if record.name == record.description:
                raise exceptions.ValidationError(
                    "Fields name and description must be different")
