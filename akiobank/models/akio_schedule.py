from odoo import api, fields, models
from _datetime import datetime


class AkioSchedule(models.Model):
    _name = 'akio.schedule'
    
    # def get_default_date(self):
    #     return datetime.now()
    
    name = fields.Char(string="Schedule Name")
    
    create_at = fields.Datetime(# Override of default create_date field from ORM
        string="Begin",
        index=True,
        copy=False
        # default=fields.DateTime.now()
        )
    
    estimate_at = fields.Datetime(
        string="Estimate End",
        copy=False,
        # default=fields.DateTime.now(),
        help="This is the my schedule.")
    
    akio_interest_rate = fields.Float(
        string="Interest rate")
    
    wallet_id = fields.Many2one(
        comodel_name='wallet',
        string="Wallet"
        )

    #===========================================================================
    # akio_debug
    #===========================================================================
    def akio_debug(self):
        pass
    
    # akio_customer_ids = fields.One2many(
    #     comodel_name = 'akio.customer',
    #     inverse_name= 'akio_schedule_id',
    #     string = "Join Customer"
    #     )
    
    #===========================================================================
    # akio_date
    #===========================================================================
    def akio_date(self):
        # date_stop_akio = self.estimade_at
         # -> datetime.datetime(2023, 6, 10, 4, 46, 41)
        print(self.read(['estimate_at']))
        print('____________________________________________________________________________________')
        # akio_today = self.estimate_at.today() #->datetime.datetime(2023, 5, 18, 8, 21, 54, 979751)
        #
        # a = fields.Date.context_today(self)# a = datetime.date(2023, 5, 18)
        # print(a) # ->2023-05-18
        
        # print("today: ",today)
    
    #===========================================================================
    # akio_add(value, *args, **kwargs)
    # value: phải khởi tạo một date hoặc datetime
    # *args: days=xxx: tham số để chạy trực tiếp đến ngày mong muốn
    #===========================================================================
    def akio_add(self):
        day1 = fields.Date.today()
        day2 = fields.Date.add(fields.Date.today(),days = 10)
        print('__________________________________________________________________________________________')
        print('day1: ',day1)
        print('day2: ',day2)
        print('__________________________________________________________________________________________')
        
    
    #===========================================================================
    # akio_context_today(record): lấy một record rồi truyền record đó vào trong ngoặcngoặc 
    #===========================================================================
    def akio_context_today(self):    
        result = fields.Date.context_today(self)
        print('__________________________________________________________________________________________')
        print('context today: ',result)
        print('__________________________________________________________________________________________')
        
    
        