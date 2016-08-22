# -*- coding: utf-8 -*-
#
#
#    Copyright (c) 2014 Carlos Sánchez Cifuentes <csanchez@grupovermon.com>
#    Copyright (c) 2015 Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
#    Copyright (c) 2015 Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>
#    Copyright (c) 2016 Serpent Consulting Services Pvt. Ltd.
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

{
    "name": "Price recalculation in sales orders",
    "version": "1.0",
    "depends": [
        "sale", 'product_uos'
    ],
    'license': 'AGPL-3',
    "author": "AvanzOSC,"
              "Serv. Tecnol. Avanzados - Pedro M. Baeza,"
              "Grupo Vermon,"
              "Odoo Community Association (OCA)",
    "category": "Sales Management",
    "website": "http://github.com/OCA/sale-workflow",
    "data": [
        "views/sale_order_view.xml",
    ],
    'installable': True,
}
