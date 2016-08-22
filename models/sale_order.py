# -*- coding: utf-8 -*-
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

from openerp import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def recalculate_prices(self):
        return self.reset_lines(price=True)

    @api.multi
    def recalculate_names(self):
        return self.reset_lines(price=False)

    @api.multi
    def reset_lines(self, price=False):
        """
        Reset lines according informations on products and price list
        :param price: boolean to indicate if we are resetting price or
                      descriptions
        """
        for line in self.mapped('order_line'):
            pricelist = self.pricelist_id
            qty = line.product_uom_qty
            product = line.product_id.with_context(lang=self.partner_id.lang,
                                                   partner=self.partner_id.id,
                                                   quantity=qty,
                                                   date=self.date_order,
                                                   pricelist=pricelist.id,
                                                   uom=line.product_uom.id)
            data = {'product_id': line.product_id.id}
            new_line = self.env['sale.order.line'].new(data)
            new_line.product_id_change()
            if price:
                line.name = new_line.name
                ac_tax = self.env['account.tax']
                line.price_unit = ac_tax._fix_tax_included_price(product.price,
                                                             product.taxes_id,
                                                             line.tax_id)
                line.product_id.uom_id = new_line.product_id.uom_id.id
            else:
                line.name = new_line.name
        return True
