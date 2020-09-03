#Luis Felipe Paternina--
from odoo import models, fields, api, _
from datetime import timedelta
import datetime


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'    
    
    task_id = fields.Many2one('project.task', 'Tarea')
    service_order = fields.Char(string="Orden del Servicio",tracking=True)
    customer = fields.Many2one('res.partner', string="Cliente", tracking=True)
    city = fields.Char(related="customer.city",string="Ciudad", tracking=True)
    approver_name = fields.Char(string="Nombre del Aprobador", tracking=True)
    approver_email = fields.Char(string="Correo del Aprobador", tracking=True)
    contract_code = fields.Char(related="customer.no_contract", string="Código del Contrato", tracking=True)
    end_date_contract = fields.Date(related="customer.end_date_contract", string="Fecha Fin del Contrato",tracking=True)
    approver_type_contract = fields.Selection(related="customer.approver_type", string="Tipo de aprobación para repuestos",tracking=True)
    brand_machine  = fields.Char(string="Marca")
    serie = fields.Char(related="equipment_id.serial_no",tracking=True)
    model_machine = fields.Char(related="equipment_id.model", tracking=True, string="Modelo")
    type_of_maintenance = fields.Selection([('correctivo','Correctivo'),('preventivo','Preventivo'),('instalacion de maquina','Instalación de Maquina'),('alistamiento','Alistamiento'),('instalacion de repuesto','Instalación de Repuesto')], string="Tipo de Mantenimiento")
    machine_location = fields.Char(string="Ubicación de la Maquina",tracking=True)    

    @api.model
    def create(self, vals):
        name = self.env['ir.sequence'].next_by_code('maintenance.request') or _('Nuevo')
        vals.update(name=name)
        return super(MaintenanceRequest, self).create(vals)      

    def write(self, vals):
        if vals.get('stage_id'):
            progress = self.env.ref('maintenance.stage_1')            
            if progress and vals.get('stage_id') == progress.id:
                self.create_task()
        if vals.get('schedule_date') or vals.get('duration'):
            self.write_task(vals)
        return super(MaintenanceRequest, self).write(vals)

    def create_task(self):
        for record in self:
            planned_date_begin = record.schedule_date
            planned_date_end = planned_date_begin
            dic = {
                'is_fsm': True,
                'project_id': self.env.ref('industry_fsm.fsm_project').id,
                'name': record.name,
                'brand': record.brand_machine,
                'model': record.model_machine,
                'serial': record.serie,
                'type_service': record.type_of_maintenance,
                'machine_location': record.machine_location,
                'customer_email': record.email_cc,
                'planned_date_begin': record.schedule_date,
                'planned_date_end': planned_date_end,
                'partner_id': record.customer.id if record.customer else False
            }
            record.task_id = self.env['project.task'].sudo().create(dic)

    def write_task(self, vals):
        for record in self:
            if record.task_id:
                planned_date_begin = vals.get('schedule_date') or record.schedule_date
                #duration = vals.get('duration') or record.duration
                try:
                    planned_date_end = planned_date_begin 
                except:
                    planned_date_end = planned_date_begin
                dic = {
                    'planned_date_begin': planned_date_begin,
                    'planned_date_end': planned_date_end
                }
                record.task_id.write(dic)
