from openerp.osv import fields, osv

AVAILABLE_STATES = [    
    ('active','Active'),
    ('done','Close'),    
]

class rdm_point_schemas(osv.osv):
    _name = "rdm.point.schemas"
    _description = "Redemption Point Schemas"
    _columns = {
        'name': fields.char('Name', size=200),
        'spend_amount': fields.float('Spend Amount'),
        'point': fields.integer('Point #'),
        'start_date': fields.date('Start Date'),
        'end_date': fields.date('End Date'),        
        'multiple': fields.boolean('Multiple'),
        'limit_point': fields.integer('Limit',help='-1 for unlimit'),
        'state': fields.selection(AVAILABLE_STATES, 'Status', size=16, readonly=True),        
    }
    
    _default = {
        'state': lambda *a: 'active',
        'limit_point': lambda *a: -1,
    }
    
rdm_point_schemas()

class rdm_point_customer(osv.osv):
    _name = "rdm.point.customer"
    _description = "Redemption Point Customer"
    _columns = {
        'customer_id': fields.many2one('rdm.customer','Customer'),
        'trans_date': fields.date('Date'),
        'point': fields.integer('Point #'),
        'remarks': fields.text('Remarks')
    }
    
rdm_point_customer()

