from odoo import fields, models, api


class EmployeeLeaveReason(models.TransientModel):
    _name = 'employee.leave.reason'

    reason = fields.Selection(string='Trạng Thái',
                              selection=[
                                  ('0', 'Đang làm việc'),
                                  ('1', 'Nghỉ Thai Sản'),
                                  ('2', 'Nghỉ Phép'),
                                  ('3', 'Nghỉ Việc')],
                              )

    def update_leave_reason(self):
        employee_id = self.env.context.get('active_id', False)

        # get record set by id. browse can have not only one parameter,
        employee_record = self.env['employee'].browse(employee_id)

        # get record set by any attribute
        # employee_record = self.env['employee'].search([('name','=','a name')])

        employee_record.write({'state': self.reason})

        # print(employee_id)
        # return True
