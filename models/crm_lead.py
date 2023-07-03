from odoo import fields, models, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    project_ids = fields.One2many('project.project', 'crm_lead_id', string='Projects')
    project_count = fields.Integer('Project Count', compute='_compute_project_count')

    def create_new_project(self):
        for lead in self:
            name = lead.name
            customer = lead.partner_id.id
            salesperson = lead.user_id.id
            project = self.env['project.project'].create({'name': name,
                                                          'partner_id': customer,
                                                          'user_id': salesperson,
                                                          'crm_lead_id': lead.id})
            return {
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'project.project',
                'res_id': project.id,
                'context': {'form_view_initial_mode': 'edit'},
            }

    def get_projects(self):
        self.ensure_one()
        action = self.env.ref('project.open_view_project_all').read()[0]
        action['domain'] = [('crm_lead_id', '=', self.id)]
        return action

    def _compute_project_count(self):
        project = self.env['project.project']
        self.project_count = project.search_count([('crm_lead_id', '=', self.id)])

    def create_new_helpdesk_ticket(self):
        for lead in self:
            name = lead.name
            contact = lead.partner_id.id
            assigned_user = lead.user_id.id
            ticket = self.env['helpdesk.ticket'].create({'name': name,
                                                         'partner_id': contact,
                                                         'user_id': assigned_user,
                                                         'description': name})
            return {
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'helpdesk.ticket',
                'res_id': ticket.id,
                'context': {'form_view_initial_mode': 'edit'},
            }
