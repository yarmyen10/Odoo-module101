# -*- coding: utf-8 -*-
# from odoo import http


# class Module101(http.Controller):
#     @http.route('/module101/module101/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module101/module101/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module101.listing', {
#             'root': '/module101/module101',
#             'objects': http.request.env['module101.module101'].search([]),
#         })

#     @http.route('/module101/module101/objects/<model("module101.module101"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module101.object', {
#             'object': obj
#         })
