#-*- coding: utf-8 -*-

{
	"name": "Library Book Order",
	"version": "2.0",
	"depends": [
		"base"
	],
	"author": "Dino Herlambang",
	"category": "Utility",
	"website": "http://instagram.com/_dinoherlambang_",
	"images": [
		"static/description/images/main_screenshot.jpg"
	],
	"license": "OPL-1",
	"summary": "Library Book Management",
	"description": "Application for Book Ordering in library",
	"data": [
		"security/groups.xml",
		"security/ir.model.access.csv",
		"view/menu.xml",
		"view/book_order.xml",
		"data/sequence_book_order.xml",
		"view/borrower.xml",
		"view/approver.xml",
		"view/book_status.xml",
		"view/stage.xml",
		"view/shelf_location.xml",
		"view/book_category.xml",
		"view/book.xml",
		"report/book_order.xml",
		"report/borrower.xml",
		"report/approver.xml",
		"report/book_status.xml",
		"report/stage.xml",
		"report/shelf_location.xml",
		"report/book_category.xml",
		"report/book.xml"
	],
	"installable": True,
	"auto_install": False,
	"application": True,
	"namespace": "dh_bk_lib"
}