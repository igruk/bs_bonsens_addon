from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    crm_lead_id = fields.Many2one('crm.lead', string='CRM Lead')

