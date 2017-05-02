# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2013 BroadTech IT Solutions.
#    (http://wwww.broadtech-innovations.com)
#    contact@boradtech-innovations.com
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

{
    'name': 'precio_en_dolares',
    'version': '10.0.0.1',
    'category': 'Product Management',
    'summary': 'Inherited for adding product changes',
    'author': 'Humanytek',
    'website': 'http://humanytek.com/',
    'depends': [
        'sale',
        'product',
    ],
    'data': [
        'views/product_view.xml',
        'views/sale_view.xml',
    ],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
