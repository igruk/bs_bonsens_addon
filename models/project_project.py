from odoo import fields, models, api


class Project(models.Model):
    _inherit = 'project.project'

    crm_lead_id = fields.Many2one('crm.lead', string='CRM Lead')
