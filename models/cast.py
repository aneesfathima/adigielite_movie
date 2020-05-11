from odoo import models, fields, api

class adigielite_movie(models.Model):
    _name = 'adigielite_movie.cast'

    actor_id = fields.Integer("Person Id")
    name = fields.Char("Name")
    movie_id = fields.Many2one('adigielite_movie.movie', string="Movie Id")