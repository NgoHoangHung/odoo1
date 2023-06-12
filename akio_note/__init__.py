from odoo import api,fields,models, _
from odoo.tools import html2plaintext
from odoo.addons.web_editor.controllers.main import handle_history_devergence

class Stage(models.Model):
    
    _name = "akio.note.stage"
    _description = "Akio Note Stage"
    _order = 'sequence'
    
    name = fields.Char('Akio Stage Name',translate = True,required = True)
    sequence = fields.Integer(default = 1)
    user_id = fields.Many2one('res.users',string='Owner',required = True,
                              ondelete = 'cascade',default = lambda self:self.env.uid)
    fold = fields.Boolean('Folded by Default')
        