from odoo import models, fields, api


class Course(models.Model):
    _name = 'course'

    name = fields.Char(string="Course", required=True)
    estimate_start = fields.Date(string='Start Estimate')
    description = fields.Text(string="Description")
    cost = fields.Integer(string='Price', required=True)
    unit_num = fields.Integer(string="Unit Num")

    class_no_ids = fields.One2many(comodel_name='class.no',
                                        inverse_name='course_id',
                                        string="Class No")


    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Course, self).create(vals)
        return record

    def write(self, vals):
        result = super(Course, self).write(vals)
        return result

    def unlink(self):
        return super(Course, self).unlink()

    def signup_learn(self):
        student = self.env['student'].browse(self.env.context.get('active_id'))
        for r in self:
            self.env.user.state == '6'
            r.amount += 1
