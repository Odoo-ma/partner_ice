# -*- coding: utf-8 -*-
{
    'name': "ICE Maroc - Montant total en lettres",

    'summary': 'Ajoute un champ ICE au contact entreprise',

    'description': """
        Ce module Odoo permet de gérer l'ICE (Identifiant Commun de l’Entreprise) pour les partenaires au Maroc.
        Il ajoute automatiquement le champ ICE aux clients et fournisseurs et l'affiche sur les factures marocaines,
        assurant la conformité légale au Maroc.
        avec validation 15 chiffres et unicité,
        ICE sera affiché sur la facture pdf
        Le montant total sera écrit en lettre sur la facture pdf
        """,

    'author': "M B",
    'license': "AGPL-3",
    'category': 'Contacts/Sales/Invoicing',
    'version': '16.0',
    'depends': ['base', 'account'], 
    'images': ['static/description/icon.png'],
    'images': ['static/description/cover.png'],
    'data': [
        'views/res_partner_view.xml',
        'views/mont_en_lettre.xml',
        'views/ice_in_invoice.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}


