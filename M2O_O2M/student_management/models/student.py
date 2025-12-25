from odoo import models, fields, api
from datetime import date

class Student(models.Model):
    _name = 'student.management.student'
    _description = 'Student Management'

    name = fields.Char(required=True)
    dob = fields.Date()

    course_id = fields.Many2one('student.management.course')
    student_age = fields.Integer(compute='_compute_student_age', store=True)

    @api.depends('dob')
    def _compute_student_age(self):
        for rec in self:
            if rec.dob:
                today = date.today()
                rec.student_age = today.year - rec.dob.year
            else:
                rec.student_age = 0
