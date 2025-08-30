import re
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    ice = fields.Char(string='ICE', size=15)

    def _check_ice_validity(self, vals):
        is_company = vals.get('is_company', self.is_company)
        ice = vals.get('ice', self.ice)
        customer_rank = vals.get('customer_rank', self.customer_rank)
        supplier_rank = vals.get('supplier_rank', self.supplier_rank)

        # Appliquer la contrainte uniquement aux entreprises clientes ou fournisseurs
        if is_company and (customer_rank > 0 or supplier_rank > 0):
            if not ice:
                raise ValidationError("Le champ ICE est obligatoire pour une entreprise client ou fournisseur.")
            if not re.fullmatch(r'\d{15}', ice):
                raise ValidationError("Le champ ICE doit contenir exactement 15 chiffres.")

            # Vérifier l’unicité de l'ICE
            duplicate = self.env['res.partner'].search([
                ('ice', '=', ice),
                ('is_company', '=', True),
                ('id', '!=', self.id)
            ], limit=1)
            if duplicate:
                raise ValidationError("Cet ICE est déjà utilisé par une autre entreprise.")

    def write(self, vals):
        for partner in self:
            partner._check_ice_validity(vals)
        return super().write(vals)

    @api.model
    def create(self, vals_list):
        if isinstance(vals_list, dict):
            vals_list = [vals_list]

        partners = super().create(vals_list)
        for partner, vals in zip(partners, vals_list):
            partner._check_ice_validity(vals)
        return partners
