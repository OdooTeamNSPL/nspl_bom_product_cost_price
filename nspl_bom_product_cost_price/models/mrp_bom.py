from odoo import models, fields, api


class MrpBom(models.Model):
    _inherit = "mrp.bom"

    product_cost_price = fields.Float(
        string="Product Cost Price",
        related="product_tmpl_id.standard_price",
        readonly=True
    )

    total_bom_cost = fields.Float(
        string="Total BoM Cost",
        compute="_compute_total_bom_cost",
        store=True
    )

    @api.depends("bom_line_ids.product_id", "bom_line_ids.product_qty", "bom_line_ids.product_id.standard_price")
    def _compute_total_bom_cost(self):
        for bom in self:
            total = 0.0
            for line in bom.bom_line_ids:
                total += (line.product_id.standard_price or 0.0) * (line.product_qty or 0.0)
            bom.total_bom_cost = total

    def name_get(self):
        result = []
        for bom in self:
            name = "BoM"
            if bom.product_tmpl_id:
                name += f" - {bom.product_tmpl_id.name}"
            elif bom.product_id:
                name += f" - {bom.product_id.display_name}"
            result.append((bom.id, name))
        return result


class MrpBomLine(models.Model):
    _inherit = "mrp.bom.line"

    component_cost_price = fields.Float(
        string="Component Cost Price",
        related="product_id.standard_price",
        readonly=True
    )
