from odoo import models, fields, api
from num2words import num2words

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    def amount_total_to_text(self):
        self.ensure_one()
        return num2words(self.amount_total, lang='fr').title() + " Dirhams"


    amount_total_words = fields.Char(
        string="Montant en lettres",
        compute="_compute_amount_total_words",
        store=False
    )

    @api.depends('amount_total', 'currency_id')
    def _compute_amount_total_words(self):
        for record in self:
            if record.currency_id:
                # Force French (fr_FR)
                record.amount_total_words = record.currency_id.with_context(lang='fr_FR').amount_to_text(record.amount_total)
                #record.amount_total_words = record.currency_id.amount_to_text(record.amount_total)
            else:
                record.amount_total_words = ''