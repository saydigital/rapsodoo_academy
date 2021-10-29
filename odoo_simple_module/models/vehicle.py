from odoo import models,fields,api


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
