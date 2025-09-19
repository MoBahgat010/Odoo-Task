# -*- coding: utf-8 -*-
# from odoo import http


# class Asset(http.Controller):
#     @http.route('/asset/asset', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asset/asset/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('asset.listing', {
#             'root': '/asset/asset',
#             'objects': http.request.env['asset.asset'].search([]),
#         })

#     @http.route('/asset/asset/objects/<model("asset.asset"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asset.object', {
#             'object': obj
#         })

