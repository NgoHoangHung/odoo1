from odoo import api, fields, models, Command


class Wallet(models.Model):
    _name = "wallet"
    _rec_name = 'akio_customer_id'

    accountnumber = fields.Char(
        string="Số Tài Khoản", compute='accountnumber_gen', store=True) 
    password = fields.Char(string="Mật Khẩu",)
    balance = fields.Float(string="Số Dư")
    bank_name = fields.Selection([('bidv', 'BIDV'),
                                 ('vtb', 'Viettin Bank'),
                                 ('acb', 'Á Châu Bank'),
                                 ('tech', 'Techcom Bank')
                                  ], string="Ngân Hàng")

    akio_customer_id = fields.Many2one(comodel_name="akio.customer",
                                       ondelete='set null',
                                       string="Khách Hàng")

    transaction_history_ids = fields.One2many('trans.history', inverse_name="wallet_id", string="Lịch sử giao dịch")
    
    akio_schedule_ids = fields.One2many(
        comodel_name='akio.schedule',
        inverse_name='wallet_id',
        string="Schedule"
        )

    @api.depends('bank_name', 'akio_customer_id.phone')
    def accountnumber_gen(self):
        for record in self:
            self.accountnumber = str(self.bank_name) + str(self.akio_customer_id.phone)
    
    def is_cal(self):
        return True if self.balance > 0 else False
    
    def akio_debug(self):
        pass
    
    #===========================================================================
    #      Command.create: 
    # Với việc thay đổi lệnh (0, 0, values): thì ta sẽ thay đổi thành Command.create
    # với ví dụ như dưới. chú ý:
    #    1, cần import Command trước khi triển khai hay chạy hàm
    #    2, ta chèn dữ liệu vào trong ngoặc là thay lệnh 0 0
    #    3, khi dùng với self.create thì bản ghi đang thao tác cũng được tạo mới.
    #       tức là ở đây sẽ có 2 bản ghi của 2 model được tạo.
    #    4, khi dùng với self.write thì bản ghi đang thao tác sẽ được coi như là sửa
    #       và chỉ tạo mới bản ghi bên phía comodel
    #    return: Thêm 1 record được tạo mới với giá trị mong muốn values.
    #===========================================================================
    def akio_create0(self):
        self.ensure_one()
        detail_vals = {
            'name':'Tiết kiệm 14 năm',
            'create_at': fields.Datetime.add(fields.Datetime.now(), days=10),
            'estimate_at': fields.Datetime.add(fields.Datetime.now(), years=10),
            'akio_interest_rate': 7.9
            }
        
        self.create({
                    'akio_schedule_ids':[
                        Command.create(detail_vals)
                ]})
        self.write({
                    'akio_schedule_ids':[
                        Command.create(detail_vals)
                ]})
        
    #===========================================================================
    # Command.update: Lệnh này cần phải có thêm một thông số là id của bản ghi nữa.
    #Chú ý rằng: mặc dù các bản ghi đang thao tác đang không có khóa liên kết tới nhưng
    # khi thử thay đổi cả những bản ghi ấy thì nó lại thay đổi được.
    #
    #  Return: Cập nhật record đã tồn tại có ID là id với giá trị sẽ cập nhật là values.
    # nếu dùng với self.create() thì không có bản ghi được tạo mới.
    #===========================================================================
    def akio_update1(self):
        self.ensure_one()
        detail_vals = {
            'name':'Tiết kiệm 16 năm',
            'create_at': fields.Datetime.add(fields.Datetime.now(), days=10),
            'estimate_at': fields.Datetime.add(fields.Datetime.now(), years=15),
            'akio_interest_rate': 8.0
            }  
        self.write({
             'akio_schedule_ids':[Command.update(17,detail_vals)]})    
    #===========================================================================
    # Command.delete:   Chỉ cần id của bản ghi
    # Return : Xóa bản ghi có mối quan hệ và xóa cả mối quan hệ với self. 
    # lệnh này là lệnh xóa, giống với unlink3 khi M2o để cascade 
    # Không thể sử dụng với create().
    #===========================================================================
    def akio_delete2(self):
        self.ensure_one()
        self.write({
             'akio_schedule_ids':[Command.delete(16)]})    
        print('xóa thành công')
    
    #===========================================================================
    # akio_unlink3: xóa bỏ mối quan hệ giữa self và bản ghi quan hệ
    #    chú ý: Trong trường hơp của mối quan hệ One2many thì các bản ghi đã cho sẽ bị xóa
    # luôn trong database nếu trường M20 kia để ondele= 'cascade' ngược lại sẽ được giữ lại
    # test thấy lệnh này cấm cho sửa trogn DB
    # nếu dùng với self.create thì không hề tạo mới.
    # tại sao self đứng từ bản gh khác mà cũng xóa được các bản ghi ko có liên kết với nó 
    #===========================================================================
    def akio_unlink3(self):
        self.ensure_one()
        self.write({
             'akio_schedule_ids':[
                 Command.unlink(12),
                 Command.unlink(13),
                 Command.unlink(14)
                 ]})           
        
