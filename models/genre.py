from odoo import models, fields, api

class adigielite_movie(models.Model):
    _name = 'adigielite_movie.genre'

    code = fields.Integer("Code")
    name = fields.Char("Name")
    movie_ids = fields.Many2many('adigielite_movie.movie', 'ade_movie_genre_rel', 'movie_id','genre_id', string="Movie Ids")