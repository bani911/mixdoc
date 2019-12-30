# -*- coding: utf-8 -*-
{
    'name': "Adhimix Documents Management",

    'summary': """
        Surat Masuk & Keluar Adhimix RMC
        dan Dokumen Manajemen""",

    'description': """
        Adhimix Document Management
    """,

    'author': "PT. Adhimix RMC Indonesia",
    'website': "http://www.adhimix.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Document Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/group.xml',
        'views/surat_masuk.xml',
        'views/master_data.xml',
        'views/surat_keluar.xml',
        'views/dokumen_file.xml',
        'views/prosedur.xml',
        'views/gudang_arsip.xml',
        # 'views/dokumen_aset.xml',
        # 'views/dokumen_akta.xml',
        # 'views/dokumen_lain.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}