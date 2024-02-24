#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class book_status(models.Model):

    _name = "dh_bk_lib.book_status"
    _description = "dh_bk_lib.book_status"

    name = fields.Char( required=True, string=_("Name"))
    note = fields.Char( string=_("Note"))


