# -*- coding: utf-8 -*-
{
    'name': "Industry Thomas",

    'summary': "Industry Thomas",

    'description': "Industry Thomas",

    'author': "Todoo SAS",
    'contributors': ['Luis Felipe Paternina lp@todoo.co'],
    'website': "http://www.todoo.co",    
    'category': 'Tools',
    'version': '13.1',

        'depends': ['base','industry_fsm','maintenance'],
    
    'data': [       
         'views/field_service.xml',
         'views/maintenance.xml',
         'views/res_partner.xml',
         'views/maintenance_equipment.xml',
        
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}
