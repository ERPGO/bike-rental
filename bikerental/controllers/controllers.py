# -*- coding: utf-8 -*-
from odoo import http

# class Bikerental(http.Controller):
#     @http.route('/bikerental/bikerental/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bikerental/bikerental/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bikerental.listing', {
#             'root': '/bikerental/bikerental',
#             'objects': http.request.env['bikerental.bikerental'].search([]),
#         })

#     @http.route('/bikerental/bikerental/objects/<model("bikerental.bikerental"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bikerental.object', {
#             'object': obj
#         })