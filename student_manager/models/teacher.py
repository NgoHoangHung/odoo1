from odoo import fields, models, api


class Teacher(models.Model):
    _name = 'teacher'

    name = fields.Char(string="Teacher Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection(string="Gender",
                              selection=[('male', 'Male'), ('female', 'Female')])
    phone = fields.Char(string="Phone", required=True)
    address = fields.Char(string="Address")
    email = fields.Char(string="Email")
    password = fields.Char(string="Password")
    salary = fields.Char(string="Salary")
    
    class_no_ids = fields.Many2many(comodel_name='class.no',
                                   relation='class_teacher_rel',
                                   column1='teacher_id',
                                   column2='class_id',
                                   string='Class'
                                   )

    @api.model
    def create(self, vals):
        # for field in ['name', 'address']:
        #     if field in vals:
        #         vals[field] = vals[field].title()
        record = super(Teacher, self).create(vals)
        return record

    def write(self, vals):
        result = super(Teacher, self).write(vals)
        return result

    # def unlink(self):
    #     return super(Teacher, self).unlink()
    
    def unlink(self):
            return super(Teacher, self).unlink()
