# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Factor Libre.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "FL Account Balance Report",
    "version": "0.1",
    "author": "Factor Libre",
    "category": "Others",
    "website": "http://www.factorlibre.com",
    "description": "Update Account Financial Report (Factor Libre Project)",
    "depends": ["base", "account_balance_reporting"],
    "init_xml": [],
    "update_xml": ["account_report_wizard.xml","wizard/wizar_print_view.xml"],
    "active": False,
    "installable": True,
}
