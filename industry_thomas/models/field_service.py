#Luis Felipe Paternina
from odoo import models, fields, api


class Todoo(models.Model):
    _inherit = 'project.task'

    phone =  fields.Char(string="Télefono",tracking=True)    
    customer_email = fields.Char(string="Correo Electrónico del Cliente",tracking=True)
    spare_parts = fields.Selection(related="partner_id.approver_type",string="Repuestos",tracking=True)
    team_to_check = fields.Many2one(string="Equipo a Revisar", tracking=True)
    serial = fields.Char(string="Serial",tracking=True)
    brand = fields.Char(string="Marca",tracking=True)
    model = fields.Char(string="Modelo",tracking=True)
    machine_location = fields.Char(string="Ubicación de la Maquina",tracking=True)
    type_request = fields.Char(string="Tipo de Solicitud",tracking=True)
    type_service = fields.Selection([('correctivo','Correctivo'),('preventivo','Preventivo'),('instalacion de maquina','Instalación de Maquina'),('alistamiento','Alistamiento'),('instalacion de repuesto','Instalación de Repuesto')], string="Tipo de Mantenimiento")
    
    
   
   
    