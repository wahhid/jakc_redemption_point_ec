from openerp.osv import fields, osv

class rdm_customer(osv.osv):
    _name = "rdm.customer"
    _inherit = "rdm.customer"
    _columns = {
        'point_customer_ids': fields.one2many('rdm.point.customer','customer_id','Points',readonly=True)
    }
rdm_customer()