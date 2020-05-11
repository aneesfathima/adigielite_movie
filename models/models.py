# -*- coding: utf-8 -*-

from odoo import models, fields, api

#from datetime
from datetime import datetime as dt
import calendar
import time
import datetime

class adigielite_movie(models.Model):
    _name = 'adigielite_movie.movie'
    _inheritence= 'video_catalog.category'

    video_id = fields.Char()
    tag_ids = fields.Integer()
    approved_flag = fields.Boolean(string='Approved Flag', default=False) 
    approved_user = fields.Integer()
    category_ids = fields.Char()
    content_rating_ids = fields.Many2one('adigielite_movie.content_rating', string="Content Rating Id")
    explicit_content = fields.Boolean(string='Explicit Content', default=True) 
    year = fields.Integer("Released Year")
    released = fields.Date(string="Released Date")
    runtime = fields.Float(string='Duration', compute="_compute_video_id")
    genre_ids = fields.Many2many('adigielite_movie.genre', 'ade_movie_genre_rel', 'genre_id','movie_id', string="Genre Ids")
    director_id = fields.Integer()
    writer_id = fields.Char()
    actor_ids = fields.Integer()
    plot = fields.Text("Plot")
    language_ids = fields.Integer()
    country_id = fields.Many2one('res.country', 'Country')
    poster = fields.Integer()
    imdb_id = fields.Char()
    type = fields.Selection([('movie', 'Movie'),('drama', 'Drama'),('serial', 'Serial')], string="Type of Video")
    title = fields.Char("Title")

