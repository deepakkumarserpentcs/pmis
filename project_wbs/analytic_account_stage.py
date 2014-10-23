# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Eficent (<http://www.eficent.com/>)
#               <contact@eficent.com>
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

import tools
from osv import fields, osv
from tools.translate import _


class analytic_account_stage(osv.osv):
    _name = 'analytic.account.stage'
    _description = 'Analytic Account Stage'
    _order = 'sequence'
    _columns = {
        'name': fields.char('Stage Name', required=True, size=64, translate=True),
        'description': fields.text('Description'),
        'sequence': fields.integer('Sequence'),
        'analytic_account_ids': fields.many2many('account.analytic.account', 'analytic_account_stage_rel', 'stage_id', 'analytic_account_id', 'Project/Analytic stages'),
        'fold': fields.boolean('Folded by Default',
                               help="This stage is not visible, "
                                    "for example in status bar or kanban view, "
                                    "when there are no records in that stage to display."),
    }
    _defaults = {
        'sequence': 1,
        'fold': False,
    }

    _order = 'sequence'

analytic_account_stage()
