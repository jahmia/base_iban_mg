# -*- coding: utf-8 -*-
import odoo
from odoo.addons.base_iban.models.res_partner_bank import _map_iban_template

_map_iban_template['mg'] = 'MG46 BBBBB SSSSS SSSSSSSSSSS SS'

odoo.addons.base_iban.models.res_partner_bank._map_iban_template = _map_iban_template
