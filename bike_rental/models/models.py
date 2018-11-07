# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class bike-rental(models.Model):
#     _name = 'bike-rental.bike-rental'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class RequestRentModel(models.Model):
    _name = 'bike_rental.bike_rental'

    name = fields.Char(string="Rental request")
    partner_id = fields.Many2one('res.partner', ondelete='set null', string="Customer", store=True)