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
    vip_customer = fields.Boolean('VIP',default = True)
    avartar = fields.Binary(string='Avatar')
    image = fields.Image(string='Icon', max_width=128, max_height=128)

    wallet_ids = fields.One2many(comodel_name="wallet",
                                 inverse_name="akio_customer_id",
                                 string="Ví"
                                 )

    _sql_constraints = [
        ('name_uniq', 'unique(phone)', 'Khách hàng chỉ có một số điện thoại'),
        # ('price_pos', 'CHECK(price >=0)', 'Product price must be positive!')
    ]

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

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        if default.get('name', False):
            return super(AkioCustomer, self).copy(default)
        try:
            default.setdefault('name', _("%s (copy)") % (self.name or ''))
            while self.env['akio.customer'].search([('name', '=', default['name'])], limit=1):
                default['name'] = _("%s (copy)") % (self.name or '')
        except ValueError:
            default['name'] = self.name
        return super(AkioCustomer, self).copy(default)

    @api.model
    #===========================================================================
    # name_create
    #===========================================================================
    def name_create(self, name):
        new_record = self.create({'name': name})
        return new_record.name_get()[0]

    def change_customer_type(self):
        records = self.env['akio.customer'].search([])
        pass
        for i in self:
            if not i.vip_customer :
                i.vip_customer = True    
    #===========================================================================
    # write
    #===========================================================================
    def write(self, vals):
        print('writing', vals)
        return super(AkioCustomer, self).write(vals)

    #===========================================================================
    # akio_find_by_id
    #===========================================================================
    def akio_find_by_id(self):
        id = self.env['akio.customer'].browse(1)
        print(id)

    #===========================================================================
    # akio_find_all
    #===========================================================================
    def akio_find_all(self):
        find_all = self.env['akio.customer'].search([])
        a = find_all.read()
        print(a)

    #===========================================================================
    # akio_read
    #===========================================================================
    def akio_read(self):
        pass
        a = self.search([])
        for i in a:
            print(i.read())
            print('________________________________')
            print(i.read(['name','gender','age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')
        
    #===========================================================================
    # akio_search_count
    #===========================================================================
    def akio_search_count(self):
        print('total curent record: ________________',self.env['akio.customer'].search_count([]))
        
    #===========================================================================
    # akio_read_group
    #===========================================================================
    def akio_read_group(self):
        records = self.env['akio.customer'].search([]).read_group(
            domain = [],
            fields=['name','age'],
            groupby=['name'],
            offset = 0,
            limit = None,
            orderby=False,
            lazy = True
            )
        for i in records:
            print(i)
            print('__________________________________________________________')
    #===========================================================================
    # find_by_domain0
    #===========================================================================
    def find_by_domain0(self):
        records = self.env['akio.customer'].search([('age','=','25')],offset = 0, limit = None,order ='name desc',count = False)
        for i in records:
            # print(i.read())
            print('________________________________')
            print(i.read(['name','gender','age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')
        
    def find_by_domain1(self):
        records = self.env['akio.customer'].search([('name','!=','A')],offset = 0, limit = None,order ='name desc',count = False)
        for i in records:
            # print(i.read())
            print('________________________________')
            print(i.read(['name','gender','age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')
        
    def find_by_domain2(self):
        records = self.env['akio.customer'].search([('age','>','25')],offset = 0, limit = None,order ='name desc',count = False)
        for i in records:
            print('________________________________')
            print(i.read(['name','gender','age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')
        
        
    def find_by_domain3(self):
        records = self.env['akio.customer'].search([('age','>=','25')],offset = 0, limit = None,order ='name desc',count = False)
        for i in records:
            print('________________________________')
            print(i.read(['name','gender','age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')
        
        
    def find_by_domain4(self):
        records = self.env['akio.customer'].search([('vip_customer','=?',False)],offset = 0, limit = None,order ='name desc',count = False)
        for i in records:
            print('________________________________')
            print(i.read(['name','gender','age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')
        
        
    def find_by_domain5(self):
        records = self.env['akio.customer'].search([('name','=like','a')],offset = 0, limit = None,order ='name desc',count = False)
        for i in records:
            print('________________________________')
            print(i.read(['name','gender','age']))
            print('________________^________________')
        print('________________________________________________________________________________________________________________________________')
        
        
        
        
        
        
        
        
