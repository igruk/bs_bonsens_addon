# -*- coding: utf-8 -*-
# from odoo import http


# class BsBonsensAddon(http.Controller):
#     @http.route('/bs_bonsens_addon/bs_bonsens_addon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bs_bonsens_addon/bs_bonsens_addon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bs_bonsens_addon.listing', {
#             'root': '/bs_bonsens_addon/bs_bonsens_addon',
#             'objects': http.request.env['bs_bonsens_addon.bs_bonsens_addon'].search([]),
#         })

#     @http.route('/bs_bonsens_addon/bs_bonsens_addon/objects/<model("bs_bonsens_addon.bs_bonsens_addon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bs_bonsens_addon.object', {
#             'object': obj
#         })
