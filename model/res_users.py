#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class res_users(models.Model):

    _name = "res.users"
    _description = "res.users"


    _inherit = "res.users"
    is_approver = fields.Boolean( string=_("Is Approver"), default=False)


