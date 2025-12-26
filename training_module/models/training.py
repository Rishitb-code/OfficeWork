from odoo import models, fields


class TrainingTrainer(models.Model):
    _name = 'training.trainer'
    _description = 'Trainer'

    name = fields.Char(string="Trainer Name", required=True)

    course_ids = fields.One2many(
        'training.course',
        'trainer_id',
        string="Courses"
    )


class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Training Course'

    name = fields.Char(string="Course Name", required=True)

    trainer_id = fields.Many2one(
        'training.trainer',
        string="Trainer"
    )

    session_ids = fields.One2many(
        'training.session',
        'course_id',
        string="Sessions"
    )

    student_ids = fields.Many2many(
        'training.student',
        string="Students"
    )


class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Training Session'

    name = fields.Char(string="Session Title")

    course_id = fields.Many2one(
        'training.course',
        string="Course",
        required=True
    )


class TrainingStudent(models.Model):
    _name = 'training.student'
    _description = 'Student'

    name = fields.Char(string="Student Name", required=True)

    course_ids = fields.Many2many(
        'training.course',
        string="Enrolled Courses"
    )
