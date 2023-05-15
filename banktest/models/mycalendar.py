# from odoo import fields, models
#
# class Mycalendar(models.Model):
#     _name = 'mycalendar'
#     _description = 'Calendar Class'
#
#     name = fields.Char(string='Calendar', required=True)
#     start_date = fields.Datetime(string='Start Date', required=True)
#     end_date = fields.Datetime(string='End Date', required=True)
#     company_id = fields.Many2one('res.company', string='Company')
#
#     _sql_constraints = [
#         ('check_dates', 'check(start_date < end_date)', 'End date must be greater than Start date!')
#     ]
