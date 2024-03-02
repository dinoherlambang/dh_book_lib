#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class borrower(models.Model):

    _name = "dh_bk_lib.borrower"
    _description = "dh_bk_lib.borrower"

    name = fields.Char( required=True, string=_("Name"))
    address = fields.Char( string=_("Address"))
    note = fields.Text( string=_("Note"))


    book_order_id = fields.Many2one(comodel_name="dh_bk_lib.book_order",  string=_("Book Order"))
