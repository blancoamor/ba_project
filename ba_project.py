# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

from openerp import models, fields, api 
from openerp import tools
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.tools.translate import _
import logging

_logger = logging.getLogger(__name__) 

class project_task(models.Model):

    _inherit = 'project.task'

    project_task_resource_id=fields.Many2one('project.task.resource',string='recurso')
    quote_task=fields.Float('Monto presuestado')
    supplier_partner_id=fields.Many2one('res.partner',string='Proveedor')
    observed_by_employee_id=fields.Many2one('hr.employee',string='Observado por')

class project_task_resource(models.Model):

    _name = 'project.task.resource'
    _description = 'project task resource'

    name=fields.Char('Nombre')
