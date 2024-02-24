#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class shelf_location(models.Model):

    _name = "dh_bk_lib.shelf_location"
    _description = "dh_bk_lib.shelf_location"

    name = fields.Char( required=True, string=_("Name"))
    note = fields.Text( string=_("Note"))


    category_id = fields.Many2one(comodel_name="dh_bk_lib.book_category",  string=_("Category"))
