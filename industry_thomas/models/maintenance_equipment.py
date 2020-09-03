#Luis Felipe Paternina--
from odoo import models, fields, api

class Todoo(models.Model):
    _inherit = 'maintenance.equipment'

    brand_maintenance = fields.Char(string="Marca", trackinig=True)