# Copyright 2021-TODAY Rapsodoo Italia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    'name': "Odoo Simple Module",
    'version': '14.0.2.0.0',
    'depends': [
        'base',
    ],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/garage_views.xml',
        'views/vehicle_views.xml',
    ],
}
