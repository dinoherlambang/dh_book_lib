#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class approver(models.Model):

    _name = "dh_bk_lib.approver"
    _description = "dh_bk_lib.approver"

    name = fields.Char( required=True, string=_("Name"))
    note = fields.Text( string=_("Note"))


