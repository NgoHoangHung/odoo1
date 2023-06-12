from odoo import models, fields, api


class Class_Detail(models.Model):
    _name = 'class.detail'

    name = fields.Integer(string='Information')
    amount = fields.Integer(string='Size',
                            compute='check_size',    
                            store=True)
    
    # state = fields.Selection(string='Status',
    #                          selection=[('0', 'Waiting'), ('1', 'Learning'),
    #                                     ('2', 'Finished'), ('3', 'Reserved'),
    #                                     ('4', 'Drop out'), ('5', 'Guess'),
    #                                     ('6', 'not pay yet')],
    #                          default='5')

    student_ids = fields.One2many(string='Student',
                                  inverse_name='class_detail_id',
                                 comodel_name='student')

    class_id = fields.Many2one(comodel_name='class.no',
                               string="Class")
    
    @api.depends('student_ids')
    def check_size(self):
      for r in self:
          r.amount = len(r.student_ids)
    
    # student_detail_line = fields.One2many(string='Student Detail',
    #                               inverse_name='class_detail_ids',
    #                              comodel_name='student.detail.line')
    #
    # course_id = fields.Many2one(comodel_name='course',
    #                             string="Course")
