# -*- coding: utf-8 -*-


def test_items_have_name_sell_in_and_quality(approved_items):
    for item in approved_items:
        assert hasattr(item, "name")
        assert hasattr(item, "sell_in")
        assert hasattr(item, "quality")
