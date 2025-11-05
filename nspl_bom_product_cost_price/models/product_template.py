from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    default_bom_id = fields.Many2one(
        'mrp.bom',
        string="BoM",
        domain="[('product_tmpl_id', '=', id)]",
        ondelete='set null'
    )

    default_bom_cost = fields.Float(
        string="BoM Cost",
        compute="_compute_default_bom_cost",
        store=True,
        readonly=False
    )

    @api.depends('default_bom_id', 'default_bom_id.total_bom_cost')
    def _compute_default_bom_cost(self):
        for rec in self:
            rec.default_bom_cost = rec.default_bom_id.total_bom_cost if rec.default_bom_id else 0.0

    @api.onchange('default_bom_id')
    def _onchange_default_bom_id(self):
        for rec in self:
            rec.default_bom_cost = rec.default_bom_id.total_bom_cost if rec.default_bom_id else 0.0
