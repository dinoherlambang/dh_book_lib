#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class book_order(models.Model):

    _name = "dh_bk_lib.book_order"
    _description = "dh_bk_lib.book_order"

    name = fields.Char( required=True, default="New", readonly=True,  string=_("Name"))
    note = fields.Html( string=_("Note"))
    description = fields.Text( string=_("Description"))
    stage_is_draft = fields.Boolean(related="stage_id.draft", store=True,  string=_("Stage Is Draft"))
    approved = fields.Boolean( string=_("Approved"))


    @api.model
    def create(self, vals):
        if not vals.get("name", False) or vals["name"] == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code("dh_bk_lib.book_order") or "Error Number!!!"
        return super(book_order, self).create(vals)

    def _get_first_stage(self):
        data_id = self.env["dh_bk_lib.stage"].sudo().search([], limit=1, order="sequence asc")
        if data_id:
            return data_id
        return False

    def action_confirm(self):
        stage = self._get_next_stage()
        self.stage_id=stage
        if self.stage_id.execute_enter and hasattr(self, self.stage_id.execute_enter) and callable(getattr(self, self.stage_id.execute_enter)):
            eval(f"self.{self.stage_id.execute_enter}()")

    def action_cancel(self):
        stage = self._get_previous_stage()
        self.stage_id=stage

    def _get_next_stage(self):
        current_stage_seq = self.stage_id.sequence
        data_id = self.env["dh_bk_lib.stage"].sudo().search([("sequence",">",current_stage_seq)], limit=1, order="sequence asc")
        if data_id:
            return data_id
        else:
            return self.stage_id

    def _get_previous_stage(self):
        current_stage_seq = self.stage_id.sequence
        data_id = self.env["dh_bk_lib.stage"].sudo().search([("sequence","<",current_stage_seq)], limit=1, order="sequence desc")
        if data_id:
            return data_id
        else:
            return self.stage_id

    def unlink(self):
        return super(book_order, self).unlink()

    book_status_id = fields.Many2one(comodel_name="dh_bk_lib.book_status",  string=_("Book Status"))
    stage_id = fields.Many2one(comodel_name="dh_bk_lib.stage",  default=_get_first_stage,  string=_("Stage"))
    location_id = fields.Many2one(comodel_name="dh_bk_lib.shelf_location",  string=_("Location"))
    book_title_id = fields.Many2one(comodel_name="dh_bk_lib.book",  string=_("Book Title"))
    borrower_ids = fields.One2many(comodel_name="dh_bk_lib.borrower",  inverse_name="book_order_id",  string=_("Borrower"))
    approver_id = fields.Many2one(comodel_name="res.users",  string=_("Approver"))
