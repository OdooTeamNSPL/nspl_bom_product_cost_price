from odoo import models, fields, api

class MrpBom(models.Model):
    _inherit = "mrp.bom"

    product_cost_price = fields.Float(
        string="Product Cost Price",
        related="product_tmpl_id.standard_price",
        readonly=True
    )

    total_bom_cost = fields.Float(
        string="Total BoM Cost", compute="_compute_total_bom_cost", store=True
    )

    @api.depends("bom_line_ids.product_id", "bom_line_ids.product_qty")
    def _compute_total_bom_cost(self):
        for bom in self:
            total = 0.0
            for line in bom.bom_line_ids:
                total += line.product_id.standard_price * line.product_qty
            bom.total_bom_cost = total


class MrpBomLine(models.Model):
    _inherit = "mrp.bom.line"

    component_cost_price = fields.Float(
        string="Component Cost Price",
        related="product_id.standard_price",
        readonly=True
    )
