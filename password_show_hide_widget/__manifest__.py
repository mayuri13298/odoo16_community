# -*- coding: utf-8 -*-
{
    'name': 'Password Show/Hide Widget',
    'version': '16.0.0.1.0',
    'category': 'All',
    'summary': "Password Show/Hide Widget",
    'description': "Password Show/Hide Widget",
    'author': '',
    "depends": ['base', 'contacts', 'hr'],
    'currency': 'EUR',
    'price': 15.00,
    "data": [
        'views/partner_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'password_show_hide_widget/static/src/js/float_range_widget.js',
            'password_show_hide_widget/static/src/css/widget.css',
            'password_show_hide_widget/static/src/xml/widget.xml',
        ],
    },
    'images': ['static/description/main.jpg'],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

