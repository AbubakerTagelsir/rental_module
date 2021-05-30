# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Furnishing(models.Model):
    _name = 'property.furnishing'
    _description = 'Furnishing'

    name = fields.Char(string='Name')
    