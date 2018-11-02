# -*- coding: utf-8 -*-
from odoo import http

# class Bike-rental(http.Controller):
#     @http.route('/bike-rental/bike-rental/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bike-rental/bike-rental/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bike-rental.listing', {
#             'root': '/bike-rental/bike-rental',
#             'objects': http.request.env['bike-rental.bike-rental'].search([]),
#         })

#     @http.route('/bike-rental/bike-rental/objects/<model("bike-rental.bike-rental"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bike-rental.object', {
#             'object': obj
#         })