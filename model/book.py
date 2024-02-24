#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class book(models.Model):

    _name = "dh_bk_lib.book"
    _description = "dh_bk_lib.book"

    name = fields.Char( required=True, string=_("Name"))
    author = fields.Char( string=_("Author"))
    year = fields.Date( string=_("Year"))
    description = fields.Text( string=_("Description"))


    category_id = fields.Many2one(comodel_name="dh_bk_lib.book_category",  string=_("Category"))
