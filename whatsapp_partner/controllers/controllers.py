# -*- coding: utf-8 -*-
# from odoo import http


# class WhatsappPartner(http.Controller):
#     @http.route('/whatsapp_partner/whatsapp_partner', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/whatsapp_partner/whatsapp_partner/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('whatsapp_partner.listing', {
#             'root': '/whatsapp_partner/whatsapp_partner',
#             'objects': http.request.env['whatsapp_partner.whatsapp_partner'].search([]),
#         })

#     @http.route('/whatsapp_partner/whatsapp_partner/objects/<model("whatsapp_partner.whatsapp_partner"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('whatsapp_partner.object', {
#             'object': obj
#         })

