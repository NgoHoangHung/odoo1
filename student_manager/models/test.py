from odoo import models, fields, api


class Test2(models.Model):
    _name = 'test2'
    # _transient= True
    
    name = fields.Char(string='Name')
    number = fields.Integer(string='Number')
    # after = fields.Integer(compute='_compute_acount')#, store=True
    after2 = fields.Integer(compute='_compute_acount1')  #
    avatar = fields.Binary(string='Avatar')
    prescription = fields.Html(string='Prescription')
    image = fields.Image(string='Logo', max_width=128, max_height=128)
    # test_id = fields.One2many(comodel_name = 'test3',inverse_name='test2_id')
    logic_bool = fields.Boolean(string="Offical", default=False)
    currency_id = fields.Many2one('res.currency', string='Currency')
    class_fund = fields.Monetary(
        string='Class Fund', currency_field='currency_id')

    plus_test_depends_context = fields.Integer(compute="test_depends_context")
    
    def test_offical(self):
        # for i in self:
        if self.logic_bool:
            self.logic_bool = False
        else:
             self.logic_bool = True
    
    # mydate = fields.Date90
    # @api.depends('number')
    def _compute_acount(self):
        for r in self:
            r.after2 = r.number * 2
            
    # @api.depends('number')
    def _compute_acount1(self):
        for r in self:
            r.after2 = r.number * 2
            
    def reset_all(self):
        records = self.search([])
        for i in records:
            i.number = 1

    def only_plus(self):
         self.number += 3

    def plus2(self):
        records = self.search([])
        for i in records:
            i.number += 2

    # def refresh(self):
        # self.env[test2].flush_model()
        # for r in self:
        #     r.number = 40
        # a = self.env.cr.execute("""
        # select * from test2
        # """)
        # print(self.env.cr.fetchall())

        # self.env.flush_all()

        # a = self.env.cr.execute("""
        # select * from test2
        # """)
        # print(self.env.cr.fetchall())

    @api.model
    def create(self, vals):
        a = self.env.cr.execute("""
        select * from test2
        """)
        print(self.env.cr.fetchall())
        record = super(Test2, self).create(vals)
        a = self.env.cr.execute("""
        select * from test2
        """)
        print(self.env.cr.fetchall())
        return record

    def up_number(self):
        all = self.env['test2'].search([])
        for r in all:
            r.number = r.number + 1

    # ('self.env.context['uid']')
    def test_depends_context(self):
        # for i in self:
        #     i.plus_test_depends_context = number*10
        pass

    # ===========================================================================
    # _selection_list: test reference
    # ===========================================================================
    def _selection_list(self):
        return [(model.model, model.name) for model in self.env['ir.model'].search([])]

    reference = fields.Reference(selection=_selection_list, string='Reference')

    # @api.model
    # def setting_init_bank_account_action(self):
    #     """ Called by the 'Bank Accounts' button of the setup bar."""
    #     view_id = self.env.ref('account.setup_bank_account_wizard').id
    #     return {'type': 'ir.actions.act_window',
    #             'name': _('Create a Bank Account'),
    #             'res_model': 'account.setup.bank.manual.config',
    #             'target': 'new',
    #             'view_mode': 'form',
    #             'views': [[view_id, 'form']],
    #             }



