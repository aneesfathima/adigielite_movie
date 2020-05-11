# -*- coding: utf-8 -*-

from odoo import models, fields, api

class adigielite_movie(models.Model):
    _name = 'adigielite_movie.content_rating'

    country_id = fields.Char()
    rating = fields.Char("Rating")


