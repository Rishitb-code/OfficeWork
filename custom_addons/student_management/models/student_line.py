from odoo import models, fields

class StudentManagementLine(models.Model):
    _name = 'student.management.line'   # 🔴 MUST MATCH EXACTLY
    _description = 'Student Line'

    student_id = fields.Many2one(
        'student.management',
        string='Student',
        ondelete='cascade'
    )

    subject = fields.Char(string='Subject')
    teacher = fields.Char(string='Teacher')
    marks = fields.Float(string='Marks')
    remarks = fields.Char(string='Remarks')
