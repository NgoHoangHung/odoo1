from odoo import models, fields, api


class Student(models.Model):
    _name = 'student'
    _description = 'origin module student'

    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection(string="Gender",
                              selection=[('male', 'Male'), ('female', 'Female')])
    phone = fields.Char(string="Phone", required=True)
    address = fields.Char(string="Address")
    email = fields.Char(string="Email")
    password = fields.Char(string="Password", default='123456', groups='student_manager.group_viinschool_manager')
    active = fields.Boolean(default=True, string="Active")

    class_detail_id = fields.Many2one(comodel_name='class.detail',
                                       string="Class")
    
    student_detail_line_ids = fields.One2many(string='Detail',
                                  inverse_name='student_id',
                                 comodel_name='student.detail.line')

    # class_id = fields.Many2one(comodel_name='class.no', string="Class")
    
    
    
    

    @api.model
    def create(self, vals):
        for field in ['name', 'address', 'email']:
            if field in vals:
                vals[field] = vals[field].title()
        record = super(Student, self).create(vals)
        return record
   
    def create_multi_test(self):
        test = [
            {'name':'hung', 'age': '29', 'gender':'male'  },
            {'name':'hung1', 'age': '29', 'gender':'male'  },
            {'name':'hung2', 'age': '29', 'gender':'male'  },
            ]
        records = self.env['student'].create(test)
        return records

    def write(self, vals):
        result = super(Student, self).write(vals)
        return result

    def unlink(self):
        return super(Student, self).unlink()

    # def update_student_password(self):
        # students = self.env['student'].browse(student_ids)
        # for student in students:
        #     student.password = new_password
        # students.flush()  # Save the changes to the database

    # def deactivate_students(self, student_ids):
    #     students = self.env['student'].browse(student_ids)
    #     students.write({'active': False})  # Set the 'active' field to False for the selected students
    
    @api.model
    def default_get(self, fields_list):
        defaults = super(Student, self).default_get(fields_list)

        # Add custom default values to the 'defaults' dictionary
        defaults.update({
            'name': 'John Doe',
            'age': 20,
            'gender': 'male',
            'phone': '1234567890',
            'address': '123 Main Street',
            'email': 'johndoe@example.com',
        })

        return defaults

