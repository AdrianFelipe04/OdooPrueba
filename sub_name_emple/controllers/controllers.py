# -*- coding: utf-8 -*-
# from odoo import http


# class SubNameEmple(http.Controller):
#     @http.route('/sub_name_emple/sub_name_emple/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sub_name_emple/sub_name_emple/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sub_name_emple.listing', {
#             'root': '/sub_name_emple/sub_name_emple',
#             'objects': http.request.env['sub_name_emple.sub_name_emple'].search([]),
#         })

#     @http.route('/sub_name_emple/sub_name_emple/objects/<model("sub_name_emple.sub_name_emple"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sub_name_emple.object', {
#             'object': obj
#         })
