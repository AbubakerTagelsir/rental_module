# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Property(models.Model):
    _name = 'property.property'
    _description = "Properties"

    name = fields.Char(string='Property Name')
    city_id = fields.Many2one('res.country.state', "City")
    area = fields.Float(string='Area')
    price_rent = fields.Integer(string='Renting Price')
    photo = fields.Binary(string='Photo', attachment=True)
    bedrooms = fields.Integer(string='Bedrooms')
    bathrooms = fields.Integer(string='Bathrooms')
    property_state = fields.Selection(string='Property State', selection=[('rented', 'Rented'), ('occupied', 'Occupied'),])
    amenties = fields.Many2many(comodel_name='property.amenities', string='Amenities')
    furnishing = fields.Many2many(comodel_name='property.furnishing', string='Furnishing')
    property_type_id = fields.Many2one(comodel_name='property.type', string="Property Type")
    