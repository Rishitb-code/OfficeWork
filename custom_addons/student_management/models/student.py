from odoo import models, fields

class StudentManagement(models.Model):
    _name = 'student.management'
    _description = 'Student Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # 🔴 ADD THIS

    name = fields.Char(string='Student Name', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True)

    line_ids = fields.One2many(
        'student.management.line',
        'student_id',
        string='Academic Records'
    )

    note = fields.Text(string='Notes')
