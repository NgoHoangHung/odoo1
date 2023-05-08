from odoo import models, fields, api


class Student_Detail_Line(models.Model):
        _name = 'student.detail.line'
        
        lecture = fields.Selection(
            string="Lecture",
            selection=[
                ('0', 'Web Basic'),
                ('1', 'Web Advance'),
                ('2', 'DataBase'),
                ('3', 'Languge Core'),
                ('4', 'Algorithm'),
                ('5', 'Frame Work')
                ]
            )
        dayoff = fields.Integer(string='Day Off')
        state = fields.Selection(
            string="State",
            selection=[
                ('0', 'Learning'),
                ('1', 'Fail'),
                ('2', 'Done'),
                ],
            default='0'
           
            )
        score1 = fields.Float(string="Score1")
        score2 = fields.Float(string="Score2")
        
        student_id = fields.Many2one(
            comodel_name="student",
            string="Student"
            )
        