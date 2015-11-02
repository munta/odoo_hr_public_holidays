#-*- coding:utf-8 -*-
#
#
#    Copyright (C) 2011,2013 Michael Telahun Makonnen <mmakonnen@gmail.com>.
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

{
    'name': 'Public Holidays',
    'version': '2.0',
    'author': 'Munta',
    'maintainer': 'munta',
    'website': 'http://muntane.es',
    'images': [],
    'category': 'Human Resources',
    'depends': ['hr'],
    'description': """
Manage Public Holidays
======================
    """,
    
    'data': [
        'view/hr_public_holidays_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
