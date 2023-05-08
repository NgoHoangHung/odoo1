from odoo import models, fields, api


class Class_No(models.Model):
    _name = 'class.no'

    name = fields.Char(string="Class Name", required=True)
    address = fields.Char(string='Place')
    
    course_id = fields.Many2one(comodel_name='course',
                                        string="Course")
    
    class_detail_ids = fields.One2many(string='Class Detail',
                                  inverse_name='class_id',
                                 comodel_name='class.detail')

    teacher_ids = fields.Many2many(comodel_name='teacher',
                                   relation='class_teacher_rel',
                                   column1='class_id',
                                   column2='teacher_id',
                                   string="Teacher")


    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Class_No, self).create(vals)
        return record

    def write(self, vals):
        result = super(Class_No, self).write(vals)
        return result

    def unlink(self):
        return super(Class_No, self).unlink()

    
            
            
