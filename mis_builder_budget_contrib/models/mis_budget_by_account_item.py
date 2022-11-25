# Copyright 2022 Camptocamp SA (https://www.camptocamp.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class MisBudgetByAccountItem(models.Model):

    _inherit = "mis.budget.by.account.item"
    _order = "budget_id, date_from, account_id, product_id"

    product_id = fields.Many2one(
        comodel_name="product.product",
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    )

    def _prepare_overlap_domain(self):
        domain = super()._prepare_overlap_domain()
        domain.extend([("product_id", "=", self.product_id.id)])
        return domain

    @api.constrains(
        "date_range_id",
        "date_from",
        "date_to",
        "budget_id",
        "analytic_account_id",
        "analytic_tag_ids",
        "account_id",
        "product_id",
    )
    def _check_dates(self):
        super()._check_dates()
        return
