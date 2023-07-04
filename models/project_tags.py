from odoo import fields, models, api


class ProjectTags(models.Model):
    _inherit = 'project.tags'

    sequence = fields.Integer(string='Sequence')
