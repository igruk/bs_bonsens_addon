from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    total = fields.Float(string='Total')
    currency = fields.Many2one('res.currency', string='Currency')
    crm_lead_id = fields.Many2one('crm.lead', string='CRM Lead')

