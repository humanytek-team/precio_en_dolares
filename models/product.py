# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2013 BroadTech IT Solutions.
#    (http://wwww.broadtech-innovations.com)
#    contact@boradtech-innovations.com
#
#    Updated by: Humanytek-Team (https://github.com/humanytek-team)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import fields, models, _


class product_template(models.Model):
    _inherit = 'product.template'

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string=_('Currency'),
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
