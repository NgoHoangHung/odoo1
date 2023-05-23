from odoo import api, fields, models, _, tools
from odoo import osv
from odoo import exceptions
from bisect import bisect_left
from collections import defaultdict
import re


class AkioCustomer(models.Model):
    _name = "akio.customer"

    name = fields.Char(string="Họ và Tên ", required=True,
                       default='Hùng đẹp trai')
    age = fields.Integer(string="Tuổi")
    phone = fields.Char('Số Điện Thoại')
    address = fields.Text(string="Địa chỉ")
    gender = fields.Selection(selection=[
        ("male", "Male"),
        ("female", "Female")
    ], string="Giới Tính")
    vip_customer = fields.Boolean('VIP', default=True)
    avartar = fields.Binary(string='Avatar')
    image = fields.Image(string='Icon', max_width=128, max_height=128)
     
    wallet_ids = fields.One2many(comodel_name="wallet",
                                 inverse_name="akio_customer_id",
                                 string="Ví"
                                 )

    # _sql_constraints = [
    #     ('name_uniq', 'unique(phone)', 'Khách hàng chỉ có một số điện thoại'),
    #     # ('price_pos', 'CHECK(price >=0)', 'Product price must be positive!')
    # ]
    
    def action_done(self):
        for rec in self:
            rec.vip_customer = False
    def akio_sudo_create(self):
        data = [
            {'name':'q3'},
            {'name':'q4'},
            ]
        return self.sudo().create(data)
    def akio_debug(self):
        print('hung')
        pass

    def _default_name(self):
        print(self.get_value())
        # return self.get_value()

    @api.model
    def create(self, vals):
        for val in vals:
            vals['name'] = vals['name'].title()
        print('creating')
        print(vals['name'])
        return super(AkioCustomer, self).create(vals)

    # @api.returns('self', lambda value: value.id)
    # def copy(self, default=None):
    #     default = dict(default or {})
    #     if default.get('name', False):
    #         print('up')
    #         return super(AkioCustomer, self).copy(default)
    #     try:
    #         default.setdefault('name', _("%s (copy)") % (self.name or ''))
    #         while self.env['akio.customer'].search([('name', '=', default['name'])], limit=1):
    #             default['name'] = _("%s (copy)") % (self.name or '')
    #     except ValueError:
    #         default['name'] = self.name
    #     print('down')
    #     return super(AkioCustomer, self).copy(default)
            
    @api.model
    # ===========================================================================
    # name_create
    # ===========================================================================
    def name_create(self, name):
        size = self.search_count([])
        data = self.default_get(['name']).get('name', False) + ' ' + str(size)
        return  self.create({'name': data})
        
        # if self.default_get(['name']) != None:
        #     input = self.default_get(['name'])
        #     size = self.search_count([])
        #     get_default_copy = input.get('name', False) + ' ' + str(size)
        # return new_record.name_get()[0]

    def change_customer_type(self):
        records = self.env['akio.customer'].search([])
        pass
        for i in self:
            if not i.vip_customer:
                i.vip_customer = True

    # ===========================================================================
    # write
    # ===========================================================================
    def write(self, vals):
        print('writing', vals)
        return super(AkioCustomer, self).write(vals)
    
    def akio_default_get(self):
        print('________________________________________________________________')
        print(self.default_get(['name']))
    
    # ===========================================================================
    # akio_find_by_id
    # ===========================================================================
    def akio_browse(self):
        print('________________________________________________________________')
        id = self.env['akio.customer'].browse(1)
        print(id)
        print('________________________________________________________________')

    # ===========================================================================
    # akio_find_all
    # ===========================================================================
        print('________________________________________________________________')

    def akio_find_all(self):
        find_all = self.env['akio.customer'].search([])
        a = find_all.read()
        print(a)
        print('________________________________________________________________')

    # ===========================================================================
    # akio_read
    # ===========================================================================
    def akio_read(self):
        print('________________________________________________________________')
        pass
        a = self.search([])
        for i in a:
            print(i.read())
            print('________________________________')
            print(i.read(['name', 'gender', 'age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')

    # ===========================================================================
    # akio_search_count
    # ===========================================================================
    def akio_search_count(self):
        print('________________________________________________________________')
        print('total curent record: ________________',
              self.env['akio.customer'].search_count([]))
        
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('total curent record: ________________',
              self.search_count([]))
        
        print('________________________________________________________________')

    # ===========================================================================
    # akio_read_group
        #   Returns: 1 danh sách các dict (một dict cho một bản ghi) gồm:
        #   các giá trị các trường được nhóm theo thuộc tính fields đã khai báo trong phần tham số
        #
        #       __domain: list of tuples specifying the search criteria:
        #       __domain': [('name', '=', 'Nguyễn Văn A3')]
        #
        #       __context: dictionary with argument like groupby
        #       __context': {'group_by': ['wallet_ids']

        #       __range: (date/datetime only) dictionary with field_name:granularity as keys

        #       mapping to a dictionary with keys: “from” (inclusive) and “to” (exclusive) mapping to a string representation of the temporal bounds of the group
    # ===========================================================================
    def akio_read_group(self):
        print('________________________________________________________________')
        records = self.env['akio.customer'].search([]).read_group(
            domain=[('age', '>', 23)],
            fields=['name', 'age', 'phone'],
            groupby=['age'],
            offset=0,
            limit=None,
            orderby=None,
            lazy=False
        )
        for i in records:
            print(i)
            print('__________________________________________________________')

    # ===========================================================================
    # find_by_domain0
    # ===========================================================================
    def find_by_domain0(self):
        print('________________________________________________________________')
        records = self.env['akio.customer'].search(
            [('age', '=', '25')], offset=0, limit=None, order='name desc', count=False)
        for i in records:
            # print(i.read())
            print('________________________________')
            print(i.read(['name', 'gender', 'age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')

    def find_by_domain1(self):
        print('________________________________________________________________')
        records = self.env['akio.customer'].search(
            [('name', '!=', 'A')], offset=0, limit=None, order='name desc', count=False)
        for i in records:
            # print(i.read())
            print('________________________________')
            print(i.read(['name', 'gender', 'age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')

    def find_by_domain2(self):
        records = self.env['akio.customer'].search(
            [('age', '>', '25')], offset=0, limit=None, order='name desc', count=False)
        for i in records:
            print('________________________________')
            print(i.read(['name', 'gender', 'age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')

    def find_by_domain3(self):
        records = self.env['akio.customer'].search(
            [('age', '>=', '25')], offset=0, limit=None, order='name desc', count=False)
        for i in records:
            print('________________________________')
            print(i.read(['name', 'gender', 'age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')

    def find_by_domain4(self):
        records = self.env['akio.customer'].search(
            [('vip_customer', '=?', False)], offset=0, limit=None, order='name desc', count=False)
        for i in records:
            print('________________________________')
            print(i.read(['name', 'gender', 'age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')

    def find_by_domain5(self):
        records = self.env['akio.customer'].search(
            [('name', '=like', 'a')], offset=0, limit=None, order='name desc', count=False)
        for i in records:
            print('________________________________')
            print(i.read(['name', 'gender', 'age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')

    # ===========================================================================
    # akio_fields
    #     Parameters
    # allfields (list) – fields to document, all if empty or not provided
    #
    # attributes (list) – attributes to return for each field, all if empty or not provided
    #
    # Returns
    # dictionary mapping field names to a dictionary mapping attributes to values.

    # ===========================================================================
    def akio_fields_get(self):
        print('__________________________________')
        records = self.env['akio.customer'].browse(1)
        print(records.fields_get(
            allfields=['name', 'age'],
            # attributes=['']
        ))
        print('__________________________________')

    def akio_unlink(self):
        print(self.unlink())

    # ___________________recordset___________________________

    # ===========================================================================
    # akio_ids: Hàm này trả về một danh sách các bản ghi bên trong recordset
    # ===========================================================================
    def akio_ids(self):
        records = self.env['akio.customer'].search([])
        print('danh sach ban ghi cua toi la:')
        print(records.ids)

    def akio_ensure_one(self):
        pass

    # ===========================================================================
    # akio_exists
    # ===========================================================================
    def akio_exists(self):
        model_wallet = self.env['wallet']
        for i in range(1, 10):
            record = model_wallet.browse(i)
            if record.exists():
                print(record.read())
            else:
                print("this record set is not found in this list %d" % i)

    # ===========================================================================
    # akio_name_get: trả về một danh sách gồm id và tên
    # ===========================================================================
    def akio_name_get(self):
        rcs = self.env['akio.customer'].search([])
        # .name_get()
        for i in rcs:
            # Trả về một danh sách một bản ghi. Đứng từ 1 bản ghi
            print(i.name_get())
        print('_________________________________________________________')
        # trả về một danh sách nhiều bản ghi. đứng từ nhiều bản ghi
        print(rcs.name_get())

    # ===========================================================================
    # akio_get_metadata
    #     Returns
    # list of ownership dictionaries for each requested record
    #
    # Return type
    # list of dictionaries with the following keys:
    #
    # id: object id
    #
    # create_uid: user who created the record
    #
    # create_date: date when the record was created
    #
    # write_uid: last user who changed the record
    #
    # write_date: date of the last change to the record
    #
    # xmlid: XML ID to use to refer to this record (if there is one), in format module.name
    #
    # xmlids: list of dict with xmlid in format module.name, and noupdate as boolean
    #
    # noupdate: A boolean telling if the record will be updated or not
    # ===========================================================================
    def akio_get_metadata(self):
        recordset = self.env['akio.customer'].search([])
        for i in recordset:
            print(i.get_metadata())
            print(
                '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^____________________________________________________')
        print('_________________________________________________________________')
        print(recordset.get_metadata)

        # ==============================Filtered=========================================
    # ===========================================================================
    # akio_filtered
    #     Model.filtered(func)
    # Return the records in self satisfying func.
    #
    # Parameters
    # func (callable or str) – a function or a dot-separated sequence of field names
    #
    # Returns
    # recordset of records satisfying func, may be empty.
    # ===========================================================================
    def akio_filtered(self):
        records = self.wallet_ids.filtered(lambda x: x.balance > 0)
        print(records.name_get())
        print(records.read())

    # ===========================================================================
    # akio_filterd_domain: truyền domain như search. 
    # lấy được recordset bên model hiện tại và model có khóa liên kết
    # ===========================================================================
    def akio_filtered_domain(self):
        records = self.wallet_ids.filtered_domain([])
        pass

    # ===========================================================================
    # akio_mapped:trả về một recordset hoặc một list. các trường quan hệ sẽ trả về recordset
    # cần lấy ra một danh sách các bản ghi của một model trước rồi mới tiến hành .mapped
    # ===========================================================================
    def akio_mapped(self):
        print('_________________________________________________________________')
        records = self.env['akio.customer'].search([])
        list_name = records.mapped('name')
     
        records_relative = records.mapped('wallet_ids')
        union_relative = records.mapped('')  # -> recordset & remove dupplicate
        print('list_name = ' , list_name)
        print('_________________________________________________________________') 
        print('records_relative = ', records_relative)
        print('_________________________________________________________________') 
        for record in records:
            
            records_relative_wallet = record.mapped('wallet_ids.akio_schedule_ids')
            print(records_relative_wallet)
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^') 
        
        print('_________________________________________________________________') 
        test = self.env['wallet'].search([])
        test_relative = test.akio_customer_id.mapped('name')
        print('akio_customer_id.mapped(name): ', test_relative)
        print('_________________________________________________________________') 

    def akio_sort(self):
        recordset = self.env['akio.customer'].search([])
        print(recordset.sorted(key=None, reverse=False).read())
        print('-------------------------------------------')
        print(recordset.sorted(key=None, reverse=True))
        print('-------------------------------------------')
        print(recordset.sorted(key='name', reverse=True))
    
    # ===========================================================================
    # #===========================================================================
    # # #===========================================================================
    # # # # end
    # # #===========================================================================
    # #===========================================================================
    #
    # ===========================================================================
