from openerp.osv import fields, osv

class rdm_point_trans(osv.osv):
    _name="rdm.point.trans"
    _description =  "Redemption Point Transaction"
    _columns = {
        'trans_date': fields.date('Date'),        
        'customer_id': fields.many2one('rdm.customer','Customer'),        
        'reward_id': fields.many2one('rdm.reward','Reward'),        
        'quantity': fields.integer('Quantity'),
        'total_point': fields.integer('Total Point'),
    }
            
rdm_point_trans()