from odoo import models,fields,api


class Garage(models.Model):
    _name = 'garage.garage'
    _description = "Garage Model"

    name = fields.Char(
        string="Name",
        required=True,
    )

    vehicles_number = fields.Integer(
        string="Vehicles Number",
    )

    ceiling_height = fields.Float(
        string="Ceiling Height",
    )

    vehicles_number_compute = fields.Integer(
        string="Vehicles Number Compute",
        compute="_compute_vechicle_numbers",
        store=True,
    )

    start_date = fields.Date(
        string="Start Date"
    )

    date_vehicles_number_change = fields.Date(
        string="Date change number"
    )

    vehicle_ids = fields.One2many(
        comodel_name='vehicle.vehicle',
        inverse_name='garage_id',
        string="Vehicles",
    )

    @api.depends('vehicle_ids')
    def _compute_vechicle_numbers(self):
        for garage in self:
            value = len(garage.vehicle_ids)
            garage.vehicles_number_compute = value

    @api.onchange('vehicles_number')
    def onchange_vehicle_number(self):
        self.date_vehicles_number_change = fields.Date.today()
