from odoo import api, fields, models


class AkioCustomer(models.Model):
    _name = "akio.customer"

    name = fields.Char(string="Họ và Tên ", required=True)
    age = fields.Integer(string="Tuổi")
    phone = fields.Char('Số Điện Thoại')
    address = fields.Text(string="Địa chỉ")
    gender = fields.Selection(selection=[
        ("male", "Male"),
        ("female", "Female")
    ], string="Giới Tính")
    wallet_ids = fields.One2many(comodel_name="wallet",
                                 inverse_name="akio_customer_id",
                                 string="Ví"
                                 )
    history_ids = fields.One2many(comodel_name="trans.history",
                                  inverse_name="akio_customer_id",
                                  string="Lịch Sử"
                                  )
    _sql_constraints = [
        ('name_uniq', 'unique(phone)', 'Khách hàng chỉ có một số điện thoại'),
        # ('price_pos', 'CHECK(price >=0)', 'Product price must be positive!')
    ]
    # state = fields.Selection(string="Trạng Thái",
    #                          selection=[
    #                              ("0", "Đang Vay"),
    #                              ("1", "Đã Trả"),
    #                              ("2", "Không Ràng Buộc")],
    #                          default="2",
    #                          readonly=False)
