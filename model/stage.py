#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class stage(models.Model):

    _name = "dh_bk_lib.stage"
    _description = "dh_bk_lib.stage"

    name = fields.Char( required=True, string=_("Name"))
    fold = fields.Boolean( string=_("Fold"))
    draft = fields.Boolean( string=_("Draft"))
    on_progress = fields.Boolean( string=_("On Progress"), default=True)
    done = fields.Boolean( string=_("Done"))
    sequence = fields.Integer( string=_("Sequence"))
    active = fields.Boolean( string=_("Active"), default=True)
    execute_enter = fields.Char( string=_("Execute Enter"))
    is_a_stage = fields.Boolean( string=_("Is A Stage"), default=True)


