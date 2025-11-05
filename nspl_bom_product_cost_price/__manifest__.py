{
    'name': 'BOM Product Cost Price',
    'version': '19.0.1',
    'summary': 'Show cost price of BoM product and total BoM cost',
    'description': """
    Display cost price of the product defined in the Bill of Materials (BoM) and the total cost of all components.

    ✔ View BoM component cost and total cost  
    ✔ Improve production cost transparency  
    ✔ Assist in pricing and margin calculations
    """,
    'category': 'Manufacturing',
    'sequence': 4,
    'author': 'Namah Softech Private Limited',
    'website': 'https://www.nspl.com',
    'license': 'LGPL-3',
    'support': 'support@namahsoftech.com',
    'price': 19.99,
    'currency': 'USD',
    'contributors': ['Rutik Patil'],
    'depends': ['mrp', 'product'],
    'data': [
        'views/mrp_bom_views.xml',
        'views/product_views.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
