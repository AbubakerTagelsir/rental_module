# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Amenities(models.Model):
    _name = 'property.amenities'
    _description = 'Amenties'

    name = fields.Char(string='Name')
    