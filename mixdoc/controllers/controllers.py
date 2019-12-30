# -*- coding: utf-8 -*-
from odoo import http

# class Mixdoc(http.Controller):
#     @http.route('/mixdoc/mixdoc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mixdoc/mixdoc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mixdoc.listing', {
#             'root': '/mixdoc/mixdoc',
#             'objects': http.request.env['mixdoc.mixdoc'].search([]),
#         })

#     @http.route('/mixdoc/mixdoc/objects/<model("mixdoc.mixdoc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mixdoc.object', {
#             'object': obj
#         })