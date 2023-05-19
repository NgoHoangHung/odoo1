from odoo import api, fields, models
from _datetime import datetime
from dateutil.relativedelta import relativedelta


class AkioSchedule(models.Model):
    _name = 'akio.schedule'
    
    # def get_default_date(self):
    #     return datetime.now()
    
    name = fields.Char(string="Schedule Name")
    
    create_at = fields.Datetime(# Override of default create_date field from ORM
        string="Begin",
        index=True,
        copy=False,
        default=fields.Datetime.now()
        )
    
    estimate_at = fields.Datetime(
        string="Estimate End",
        copy=False,
        default=fields.Datetime.now(),
        help="This is the my schedule.")
    
    akio_interest_rate = fields.Float(
        string="Interest rate")
    
    wallet_id = fields.Many2one(
        comodel_name='wallet',
        string="Wallet",
        ondelete = 'restrict'
        )
    
    @api.model_create_multi
    def create(self, vals):
        return super(AkioSchedule, self).create(vals) 
    
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
        print('____________________________________________________________________________________')
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
        day2 = fields.Date.add(fields.Date.today(), days=10)
      
        print('_____________________________________Date _____________________________________________________')
        print('day1: ', day1)
        print('day2: ', day2)
        print('type day2: ', type(day2))
        print('__________________________________________________________________________________________')
    
    #===========================================================================
    # akio_subtract:Nguợc laji với add là hàm trừ ngày
    # Cấu trúc:
    # static subtract(value, *args, **kwargs)[source]: Return the difference between value and a relativedelta.
    # Trả về một giá trị là hiệu của ngày 
    # Parameters
    # value – phải khởi tạo một date hoặc datetime: fields.Date.today() với date và fields.DateTime.now()
    #
    # args – positional args to pass directly to relativedelta.
    #
    # kwargs – keyword args to pass directly to relativedelta.
    #
    # Returns the resulting date/datetime.
    # 
    #===========================================================================
    def akio_subtract(self):
        print('__________________________________________________________________________________________')
        input = fields.Date.today()
        output = fields.Date.subtract(input, days=3)
        print('input: ' , input)
        print('output: ' , output)
        print('type input:', type(input))
        print('type output:', type(output))
        print('__________________________________________________________________________________________')

    #===========================================================================
    # akio_context_today(record): lấy một record rồi truyền record đó vào trong ngoặcngoặc 
    #===========================================================================
    def akio_context_today(self): 
        result = fields.Date.context_today(self)
        print('__________________________________________________________________________________________')
        print('context today: ', result)
        print('__________________________________________________________________________________________')
        
    #===========================================================================
    # akio_to_date: giá trị truyền vào là string và phải có định dạng ngày tháng năm
    #===========================================================================
    def akio_to_date(self):
        y = '2023-05-12'
        x = fields.Date.to_date(y)
        print('__________________________________________________________________________________________')
        print('type y:', type(y))
        print('type x:', type(x))
        print(x)
        print('__________________________________________________________________________________________')
        
    #===========================================================================
    # akio_to_string(value): giá trị nhập vào là date hoặc datetime. nếu là datetime thì output sẽ cắt bỏ giớ phút giây đi
    # tỏng ví dụ dưới, ta lấy luôn self, tức là bản ghi đang có nút ta ấn và .đến giá trị có kiểu là date hoặc datetime.
    # trong ví dụ này thì là datetime
    #===========================================================================
    def akio_to_string(self):
        print('__________________________________________________________________________________________')
        input = self.create_at
        output = fields.Date.to_string(input)
        print('input: ' , input)
        print('output: ' , output)
        print('type input:', type(input))
        print('type output:', type(output))
        print('__________________________________________________________________________________________')
    
    #===========================================================================
    # start_of(value, granularity): 
    # value là giá trị khởi tạo.
    # granularity là kiểu của khoảng thời gian trong chuỗi ta có thể truyền:'year', 'quarter', 'month', 'week' or 'day'
    # return a date/datetime object corresponding to the start of the specified period.
    #===========================================================================
    def akio_start_of(self):
        print('__________________________________________________________________________________________')
        input = fields.Date.today()
        output = fields.Date.start_of(input, 'year')
        print('input: ' , input)
        print('output: ' , output)
        print('type input:', type(input))
        print('type output:', type(output))
        print('quarter:', fields.Date.start_of(input, 'quarter'))
        print('month:', fields.Date.start_of(input, 'month'))
        print('week:', fields.Date.start_of(input, 'week'))
        print('day:', fields.Date.start_of(input, 'day'))
        print('__________________________________________________________________________________________')
        
    #===========================================================================
    # akio_end_of
    #===========================================================================
    def akio_end_of(self):
        print('__________________________________________________________________________________________')
        input = fields.Date.today()
        output = fields.Date.end_of(input, 'year')
        print('input: ' , input)
        print('output: ' , output)
        print('type input:', type(input))
        print('type output:', type(output))
        print('quarter:', fields.Date.end_of(input, 'quarter'))
        print('month:', fields.Date.end_of(input, 'month'))
        print('week:', fields.Date.end_of(input, 'week'))
        print('day:', fields.Date.end_of(input, 'day'))
        print('__________________________________________________________________________________________')
    
    def akio_relativedelta(self):
        input = fields.Date.today() 
        x = input - relativedelta(days=1)
        y = input + relativedelta(days=1)
        z = x + relativedelta(days=1)
        print('__________________________________________________________________________________________')
        print ("x = " , x)
        print ("y = " , y)
        print ("z = " , z)
        print('__________________________________________________________________________________________')
        
  #=============================================================================
  #=============================================================================
  #=============================================================================
  #=============================================================================
  #=============================================================================
  # # # # # DATE TIME
  #=============================================================================
  #=============================================================================
  #=============================================================================
  #=============================================================================
  #=============================================================================
    def akio_add_dt(self):
        input = fields.Datetime.now()
        datetime_input_add = fields.Datetime.add(input, days=10, hours=2, minutes=20, seconds=44)
        print('_____________________________________Date Time_____________________________________________________')
        print('datetime_input_add: ', datetime_input_add)
        print('__________________________________________________________________________________________')
        
    #===========================================================================
    # context_timestamp(record, timestamp): đầu vào là một bản ghi 
    # phương thức này không có nghĩa với người dùng như là một khởi tạo mặc định
    # do các  trường datetime tự động chuyển đổi trên màn hình phía client. 
    # Với các giá  trị mặc định thì now sẽ được sử dụng thay thế  
    #
    # Tham số truyền vào là 1 bản ghi và 
    #===========================================================================
    def akio_context_time(self):
        # timestamp = fields.Datetime.now()
        timestamp = datetime(2023, 5, 18, 10, 30, 0)
        client_timestamp = fields.Datetime.context_timestamp(self, timestamp)
        print('_____________________________________Date Time____________________________________________')
        print('timestamp: ', timestamp)
        print('client_timestamp: ', client_timestamp)
        print('__________________________________________________________________________________________')
        
    #===========================================================================
    # end_of:
    #===========================================================================
    def akio_end_of_dt(self):
        print('_____________________________________Date Time____________________________________________')

        input = fields.Datetime.now()
        output = fields.Datetime.end_of(input, 'year')
        print('input: ' , input)
        print('output: ' , output)
        print('type input:', type(input))
        print('type output:', type(output))
        print('quarter:', fields.Datetime.end_of(input, 'quarter'))
        print('month:', fields.Datetime.end_of(input, 'month'))
        print('week:', fields.Datetime.end_of(input, 'week'))
        print('day:', fields.Datetime.end_of(input, 'day'))
        print('day:', fields.Datetime.end_of(input, 'hour'))
        print('__________________________________________________________________________________________')
    
    #===========================================================================
    # akio_to_datetime
    #===========================================================================
    def akio_to_datetime(self):
        y = '2023-05-12 10:22:11'
        x = fields.Datetime.to_datetime(y)
        print('_____________________________________Date Time____________________________________________')
        print('type x:', type(x))
        print('type y:', type(y))
        print(x)
        print('__________________________________________________________________________________________')
    
    def akio_today_datetime(self):
        x = fields.Datetime.today()
        print('_____________________________________Date Time____________________________________________')
        print('type x:', type(x))
        print(x)
        print('__________________________________________________________________________________________')
    
#===============================================================================
# end
#===============================================================================
# #===============================================================================
#===============================================================================
# #===============================================================================
#===============================================================================
#===============================================================================
