# -*- coding: utf-8 -*-

from odoo import models, fields, api

class adigielite_movie(models.Model):
    _name = 'adigielite_movie.video'

    movie_id = fields.Many2one('adigielite_movie.movie', string="Movie Id")
    quality = fields.Integer()
    video_size = fields.Integer()
