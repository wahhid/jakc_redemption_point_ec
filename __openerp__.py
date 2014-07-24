{
    'name' : 'Redemption and Point Management - Point Module',
    'version' : '1.0',
    'author' : 'JakC',
    'category' : 'Generic Modules/Redemption And Point Management',
    'depends' : ['base_setup','base','jakc_redemption_customer'],
    'init_xml' : [],
    'data' : [			
        'jakc_redemption_point_view.xml',
        'jakc_redemption_point_menu.xml',        
        'jakc_redemption_point_trans_view.xml',
        'jakc_redemption_point_trans_menu.xml',                      
        'jakc_redemption_customer_view.xml',                      
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}