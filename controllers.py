# -*- coding: utf-8 -*-
from openerp import http

# class OdooAventisCustomer(http.Controller):
#     @http.route('/odoo_aventis_customer/odoo_aventis_customer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_aventis_customer/odoo_aventis_customer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_aventis_customer.listing', {
#             'root': '/odoo_aventis_customer/odoo_aventis_customer',
#             'objects': http.request.env['odoo_aventis_customer.odoo_aventis_customer'].search([]),
#         })

#     @http.route('/odoo_aventis_customer/odoo_aventis_customer/objects/<model("odoo_aventis_customer.odoo_aventis_customer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_aventis_customer.object', {
#             'object': obj
#         })