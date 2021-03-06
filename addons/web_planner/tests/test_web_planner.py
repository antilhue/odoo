# -*- coding: utf-8 -*-


from odoo.tests.common import TransactionCase
from odoo.addons.web_planner.models.web_planner import Planner


class TestWebPlanner(TransactionCase):

    def test_00(self):
        #default view
        action = self.env["ir.actions.act_window"].create(
            {
                "name": "test_web_planner_00",
                "res_model": "res.partner",
                "view_mode": "tree",
            }
        )

        self.env["ir.model.data"].create(
            {
                "name": "test_00",
                "module": "web_planner",
                "model": "ir.actions.act_window",
                "res_id": action.id,
            }
        )

        self.assertEqual(
            Planner.prepare_backend_url(self, "web_planner.test_00"),
            "/web#view_type=list&action=%s" % action.id,
        )

    def test_01(self):
        #bad choise of view_type
        action = self.env["ir.actions.act_window"].create(
            {
                "name": "test_web_planner_01",
                "res_model": "res.partner",
                "view_mode": "tree",
            }
        )

        self.env["ir.model.data"].create(
            {
                "name": "test_01",
                "module": "web_planner",
                "model": "ir.actions.act_window",
                "res_id": action.id,
            }
        )

        self.assertEqual(
            Planner.prepare_backend_url(self, "web_planner.test_01", 'form'),
            "/web#view_type=list&action=%s" % action.id,
        )
    
    def test_02(self):
        #choose the second view_mode
        action = self.env["ir.actions.act_window"].create(
            {
                "name": "test_web_planner_02",
                "res_model": "res.partner",
                "view_mode": "tree,form",
            }
        )

        self.env["ir.model.data"].create(
            {
                "name": "test_02",
                "module": "web_planner",
                "model": "ir.actions.act_window",
                "res_id": action.id,
            }
        )

        self.assertEqual(
            Planner.prepare_backend_url(self, "web_planner.test_02", 'form'),
            "/web#view_type=form&action=%s" % action.id,
        )
    
    def test_03(self):
        #bad xml_id
        action = self.env["ir.actions.act_window"].create(
            {
                "name": "test_web_planner_03",
                "res_model": "res.partner",
                "view_mode": "tree,form",
            }
        )

        self.env["ir.model.data"].create(
            {
                "name": "test_03",
                "module": "web_planner",
                "model": "ir.actions.act_window",
                "res_id": action.id,
            }
        )

        self.assertEqual(
            Planner.prepare_backend_url(self, "web_planner.bad_xml_id", 'form'),
            "/web#view_type=list&model=ir.module.module",
        )

