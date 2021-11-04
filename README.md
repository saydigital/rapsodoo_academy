# Odoo Simple Module


## Table of Contents

- [Introduction and Technology stack](#Introduction-and-Technology-stack)
- [Actual Version](#Actual-version)
- [Relational Fields in Odoo](#Relational-Fields-in-Odoo)
- [ORM Operations](#ORM-Operations)


## Introduction and Technology stack

"Odoo Simple Module" is an educational module for learning to play with Odoo. The aim is to provide programming basics with a study example.


### Tech stack: 
- Python
- HTML / CSS / XML 
- Javascript 
- PostgreSQL 


## Actual Version 

The actual version is the 14.0.2.0.0. 

Main features: 

(Aggiungere features finali di questa versione)

	

## Relational Fields in Odoo 

Relational fields in Odoo are used to link one model with another. Also, the use of relational fields is the main tool that makes the integration between different models possible, which is a very important and useful feature in Odoo. The three types of Relational fields in Odoo are:

* Many2one field
* One2many field
* Many2many field

### Many2one

A Many2one field relates the current model's record with one among the many records of the second model, called the co-model

```
field_id  = fields.Many2one(‘comodel.name’, ‘Field Name’)
```

If we check the database table of the model, the column corresponding to the Many2one field will be of the type integer and will contain an integer value, which is the id of the record of the co-model. You can also easily access the fields of the related record as:

```
filed_id.name
```

For example, if we want to relate our model **vehicle.vehicle**  with the **garage.garage** model, we can define a Many2one field called 'garage_id' as: 

```
garage_id = fields.Many2one(comodel_name='garage.garage')
```

### One2many

An One2many field relation is the inverse of the Many2one relation. The field relates one record of the co-model to many records of the model. One2many fields have the _ids suffix. 
For example, we want to relate our garage to the "customer.customer".

```
garage_ids = fields.One2many(comodel_name='customer.customer')
```

## ORM Operations

(Breve descrizione di cosa vuol dire "ORM") 


### onChange

In the form views where the field appears, the method will be called when one of the given fields is modified. The method is invoked on a pseudo-record that contains the values present in the form. Field assignments on that record are automatically sent back to the client

```
@api.onchange('vehicles_number')
   def onchange_vehicle_number(self):
       self.date_vehicles_number_change = fields.Date.today()
```

Since @onchange returns a recordset of pseudo-records, calling any one of the CRUD methods (create(), read(), write(), unlink()) on the aforementioned recordset is undefined behaviour, as they potentially do not exist in the database yet. Instead, simply set the record’s field like shown in the example above or call the update() method.

### depends

Return a decorator that specifies the field dependencies of a “compute” method. Each argument must be a string that consists in a dot-separated sequence of field names. 

```
@api.depends('vehicle_ids')
def _compute_vechicle_numbers(self):
	for garage in self:
   		value = len(garage.vehicle_ids)
      garage.vehicles_number_compute = value
```

### Write

### Search




