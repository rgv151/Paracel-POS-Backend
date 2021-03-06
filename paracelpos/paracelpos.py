##############################################################################
#
# Copyright (c) 2012 RiTH-Tech (http://rith-tech.com). All Right Reserved
#
# Author : Huy Doan (huy.doan@rith-tech.com)
#
##############################################################################

from osv import fields, osv

class pos_floor(osv.osv):
    """Restaunrent/cafe floor"""
    _name = 'pos.floor'
    _description = "Floor"
    
    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'description': fields.char('Description', size=100),
	'table_ids': fields.one2many('pos.table', 'floor_id', 'Tables'),
	'icon': fields.binary('Icon'),
	'background': fields.binary('Background'),
        'state': fields.selection([('draft', 'Draft'),
                                   ('open', 'Opened'),
                                   ('close', 'Closed')],
                                  'State', readonly=True),
    }
    _defaults = {
	'state': 'draft',
    }

    def set_open(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'open'}, context=context)
        return True

    def set_close(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'close'}, context=context)
        return True
pos_floor()

class pos_table(osv.osv):
    """Restaunrent/cafe table"""
    _name = 'pos.table'
    _description = "Table"
    
    _columns = {
        'name': fields.char("Name", size=64, required=True),
        'floor_id': fields.many2one('pos.floor', "Floor", required=True),
	'description': fields.char('Description', size=100),
	'icon': fields.binary('Icon'),
        'state': fields.selection([
            ('draft', 'Draft'),
            ('open', 'Opened'),
            ('close', 'Closed')],
            'State', readonly=True),
        'x': fields.integer('X coordinate'),
        'y': fields.integer('Y coordinate'),
    }
    _defaults = {
	'state': 'draft',
    }
    def set_open(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'open'}, context=context)
        return True

    def set_close(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'close'}, context=context)
        return True
pos_table()

class pos_order(osv.osv):
    _inherit = 'pos.order'
    _columns = {
        'table_id': fields.many2one('pos.table', 'Table', required=False, readonly=False),
    }
pos_order()
