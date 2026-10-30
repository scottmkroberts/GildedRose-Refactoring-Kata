# -*- coding: utf-8 -*-
from gilded_rose import GildedRose


def test_items_have_name_sell_in_and_quality(approved_items):
    for item in approved_items:
        assert hasattr(item, "name")
        assert hasattr(item, "sell_in")
        assert hasattr(item, "quality")


def test_quality_never_exceeds_50(
    aged_brie_at_cap, backstage_pass_10_days, backstage_pass_5_days
):
    items = [aged_brie_at_cap, backstage_pass_10_days, backstage_pass_5_days]
    GildedRose(items).update_quality()
    for item in items:
        assert item.quality <= 50


def test_sulfuras_quality_stays_at_80(sulfuras_not_yet_due, sulfuras_past_due):
    items = [sulfuras_not_yet_due, sulfuras_past_due]
    GildedRose(items).update_quality()
    for item in items:
        assert item.quality == 80


def test_quality_never_negative(vest_at_floor, elixir_past_due_near_floor):
    items = [vest_at_floor, elixir_past_due_near_floor]
    GildedRose(items).update_quality()
    for item in items:
        assert item.quality >= 0
