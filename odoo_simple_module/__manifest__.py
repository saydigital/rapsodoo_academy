
{
    'name': "Odoo Simple Module",
    'version': '14.0.1.0.0',
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
