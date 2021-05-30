# -*- coding: utf-8 -*-
{
    'name': "Rental Module",

    'summary': """
        Real Estate Rent Management""",

    'description': """
        This module provide rental system for real estate properties.
    """,

    'author': "Abubaker Tagelsir <abubaker.tagelsir>",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Others',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/furnishing.xml',
        'views/amenities.xml',
        'views/property_type.xml',
        'views/property.xml',
        ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'application': True,
    'installable': True
}
