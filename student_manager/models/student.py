from odoo import models, fields, api


class Student(models.Model):
    _name = 'student'
    _description = 'origin module student'
    # _log_access = True
    # _transient= True

    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection(string="Gender",
                              selection=[('male', 'Male'), ('female', 'Female')])
    phone = fields.Char(string="Phone", required=True)
    address = fields.Char(string="Address")
    email = fields.Char(string="Email")
    password = fields.Char(string="Password", default='123456',
                           groups='student_manager.group_viinschool_manager')
    active = fields.Boolean(default=True, string="Active")

    class_detail_id = fields.Many2one(comodel_name='class.detail',
                                      string="Class")

    student_detail_line_ids = fields.One2many(string='Detail',
                                              inverse_name='student_id',
                                              comodel_name='student.detail.line')

    # class_id = fields.Many2one(comodel_name='class.no', string="Class")

    # @api.model
    # def create(self, vals):
    #     for field in ['name', 'address', 'email']:
    #         if field in vals:
    #             vals[field] = vals[field].title()
    #     record = super(Student, self).create(vals)
    #     return record

    def test_create_command0(self):
        self.ensure_one()
        detail_vals = {
            'lecture': 0,
            'state': '2'
        }
        self.write({
            'student_detail_line_ids': [(0, 0, detail_vals)]
        })

    # ===========================================================================
    #  test_update_command1:  Cập nhật record đã tồn tại có ID là id với giá trị sẽ cập nhật là values.
    #                         Không thể sử dụng với create()
    # ===========================================================================
    def test_update_command1(self):
        # records = self.env['student.detail.line']
        # edit_fields = {
        #     'score1': 5.4,
        #     'state': '1'
        # }
        # # id_search = records.search(['id','=','active_id']).id
        # self.write({
        #     'student_detail_line_ids': [(1, 2, edit_fields)]
        # })
        
        
        
        pass
        
        
       

    # ===========================================================================
    # test_delete_command2
        '''
        Xóa bản ghi đã tồn tại có ID là id khỏi recordset hiện tại, 
        sau đó xóa luôn record đó dưới Database. 
        Không thể sử dụng với create().
        '''
    # ===========================================================================

    def test_delete_command2(self):
        self.write({
            'student_detail_line_ids': [(2, 3, 0)]
        })

    # ===========================================================================
    # test_delete_command3
        # '''
        #     Xóa bản ghi đã tồn tại có ID là id khỏi recordset hiện tại,
        #     nhưng không xóa record đó dưới Database.
        #     Không thể sử dụng với create().
        # '''
    # ===========================================================================

    def test_delete_command3(self):
        self.write({
            'student_detail_line_ids': [(3, 5, 0)]
        })

    # ===========================================================================
    # test_append_command4
    # Thêm record đã tồn tại có ID là id vào recordset hiện tại. Gần giống với lệnh 0,
    # nhưng lệnh 0 là thêm và tạo mới. Còn lệnh 4 là chỉ thêm 1 record đã có sẵn
    # ===========================================================================

    def test_append_command4(self):
        self.write({
            'student_detail_line_ids': [(4, 6, 0)]
        })

    def test_delete_command5(self):
        print('hung dep trai1')

    def test_edit_command6(self):
        print('hung dep trai1')

    def create_multi_test(self):
        test = [
            {'name': 'hung', 'age': '29', 'gender': 'male'},
            {'name': 'hung1', 'age': '29', 'gender': 'male'},
            {'name': 'hung2', 'age': '29', 'gender': 'male'},
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
            # 'address': '123 Main Street',
            # 'email': 'johndoe@example.com',
        })

        return defaults

    def test_search_count(self):
        student_record_count = self.env['student'].search_count([])
        print(student_record_count)
        return student_record_count

    def test_read_fail(self):
        records = self.env['student'].search([])
        return records

    def custom_method(self):
        self.ensure_one()
        print(self.name)
        print(self.age)

    def delete_by_score_zero(self):
        records = self.student_detail_line_ids.filtered(
            lambda x: x.score1 == 0)
        records.unlink()
