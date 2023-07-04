from odoo import fields, models, api


class ProjectTags(models.Model):
    _inherit = 'crm.tag'

    sequence = fields.Integer(string='Sequence')
