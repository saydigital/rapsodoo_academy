# Copyright 2021-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import models,fields,api
from odoo.exceptions import ValidationError

class Vehicle(models.Model):
    _name = 'vehicle.vehicle'
    _description = "Vehicle Model"

    name = fields.Char(
        string="Name",
        required=True,
    )
    
    garage_id = fields.Many2one(
        comodel_name='garage.garage',
        string="Garage"
    )

    #New features
    license_plate = fields.Char(
        string="License Plate",
        required=True
    )
    
    daily_fare = fields.Float(
        string="Daily Fare"
    )
    
    vehicle_type = fields.Selection([("motorcycle", "Motorcycle"), ("car","Car")])
        
    _sql_constraints =  [ ('license_plate','UNIQUE(license_plate)','The license plate must be unique') ]
    
    @api.constrains('license_plate')
    def _check_license_plate(self):
        if len(self.license_plate) < 5: 
            raise ValidationError("The license plate must be at least 5 characters long!")   
    
    @api.onchange('vehicle_type')
    def onchange_vehicle_number(self):
        if self.vehicle_type == 'motorcycle': 
            self.daily_fare = 50
        elif self.vehicle_type == 'car': 
            self.daily_fare = 25

    @api.model
    def create(self, values):
        search_domain = [('id', '=', values['garage_id'])]
        garage_id = self.env['garage.garage'].search(search_domain)
                
        if garage_id.vehicles_number < garage_id.vehicles_number_compute: 
            raise ValidationError("Maximum number of vehicles allowed!")
        
        values.update({'license_plate': values['license_plate'].upper()})
        
        return super(Vehicle, self).create(values)