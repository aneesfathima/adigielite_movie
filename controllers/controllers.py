# -*- coding: utf-8 -*-
from odoo import http

# class AdigieliteMovie(http.Controller):
#     @http.route('/adigielite_movie/adigielite_movie/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/adigielite_movie/adigielite_movie/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('adigielite_movie.listing', {
#             'root': '/adigielite_movie/adigielite_movie',
#             'objects': http.request.env['adigielite_movie.adigielite_movie'].search([]),
#         })

#     @http.route('/adigielite_movie/adigielite_movie/objects/<model("adigielite_movie.adigielite_movie"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('adigielite_movie.object', {
#             'object': obj
#         })