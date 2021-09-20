# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EmpleadoTemplate(models.Model):
    #_name = 'new_module.new_module'
    _inherit = 'hr.employee'

    sub_name_empl = fields.Char(string="Sub Nombre", required=False)
