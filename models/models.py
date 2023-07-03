# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class bs_bonsens_addon(models.Model):
#     _name = 'bs_bonsens_addon.bs_bonsens_addon'
#     _description = 'bs_bonsens_addon.bs_bonsens_addon'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
