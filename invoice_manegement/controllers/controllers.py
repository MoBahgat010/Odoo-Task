# -*- coding: utf-8 -*-
# from odoo import http


# class InvoiceManegement(http.Controller):
#     @http.route('/invoice_manegement/invoice_manegement', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_manegement/invoice_manegement/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_manegement.listing', {
#             'root': '/invoice_manegement/invoice_manegement',
#             'objects': http.request.env['invoice_manegement.invoice_manegement'].search([]),
#         })

#     @http.route('/invoice_manegement/invoice_manegement/objects/<model("invoice_manegement.invoice_manegement"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_manegement.object', {
#             'object': obj
#         })

