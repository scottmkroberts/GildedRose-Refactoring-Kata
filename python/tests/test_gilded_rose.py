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


def test_sulfuras_never_sold_or_decreases_in_quality(
    sulfuras_not_yet_due, sulfuras_past_due
):
    items = [sulfuras_not_yet_due, sulfuras_past_due]
    before = [(item.sell_in, item.quality) for item in items]

    GildedRose(items).update_quality()

    for item, (sell_in_before, quality_before) in zip(items, before):
        assert item.sell_in == sell_in_before
        assert item.quality == quality_before == 80


def test_quality_never_negative(vest_at_floor, elixir_past_due_near_floor):
    items = [vest_at_floor, elixir_past_due_near_floor]
    GildedRose(items).update_quality()
    for item in items:
        assert item.quality >= 0


def test_sell_in_and_quality_decrease_by_one_for_normal_items(vest, elixir):
    items = [vest, elixir]
    before = [(item.sell_in, item.quality) for item in items]

    GildedRose(items).update_quality()

    for item, (sell_in_before, quality_before) in zip(items, before):
        assert item.sell_in == sell_in_before - 1
        assert item.quality == quality_before - 1


def test_aged_brie_quality_increases_as_it_ages(aged_brie):
    sell_in_before, quality_before = aged_brie.sell_in, aged_brie.quality

    GildedRose([aged_brie]).update_quality()

    assert aged_brie.sell_in == sell_in_before - 1
    assert aged_brie.quality == quality_before + 1


def test_quality_degrades_twice_as_fast_past_sell_by_date(vest_past_due):
    quality_before = vest_past_due.quality

    GildedRose([vest_past_due]).update_quality()

    assert vest_past_due.quality == quality_before - 2


def test_aged_brie_past_sell_by_date_currently_doubles_increase(aged_brie_past_due):
    # Matches current gilded_rose.py behavior (not necessarily intended):
    # the "twice as fast" past-due rule is applied symmetrically, so Brie's
    # increase also doubles to +2/day instead of staying at +1/day. See
    # dev notes re: possible spec ambiguity before changing this.
    quality_before = aged_brie_past_due.quality

    GildedRose([aged_brie_past_due]).update_quality()

    assert aged_brie_past_due.quality == quality_before + 2


def test_backstage_pass_quality_increases_by_one_when_far_from_concert(
    backstage_pass_15_days,
):
    quality_before = backstage_pass_15_days.quality

    GildedRose([backstage_pass_15_days]).update_quality()

    assert backstage_pass_15_days.quality == quality_before + 1


def test_backstage_pass_quality_increases_by_two_within_ten_days(
    backstage_pass_10_days_with_room,
):
    quality_before = backstage_pass_10_days_with_room.quality

    GildedRose([backstage_pass_10_days_with_room]).update_quality()

    assert backstage_pass_10_days_with_room.quality == quality_before + 2


def test_backstage_pass_quality_increases_by_three_within_five_days(
    backstage_pass_5_days_with_room,
):
    quality_before = backstage_pass_5_days_with_room.quality

    GildedRose([backstage_pass_5_days_with_room]).update_quality()

    assert backstage_pass_5_days_with_room.quality == quality_before + 3


def test_backstage_pass_quality_drops_to_zero_after_concert(
    backstage_pass_day_of_concert,
):
    GildedRose([backstage_pass_day_of_concert]).update_quality()

    assert backstage_pass_day_of_concert.quality == 0


def test_backstage_pass_quality_stays_zero_after_concert(backstage_pass_after_concert):
    GildedRose([backstage_pass_after_concert]).update_quality()

    assert backstage_pass_after_concert.quality == 0


def test_conjured_items_degrade_twice_as_fast(conjured_mana_cake):
    # Not yet implemented: gilded_rose.py currently has no special case for
    # Conjured items, so this fails (-1/day like a normal item) until that
    # rule is added.
    quality_before = conjured_mana_cake.quality

    GildedRose([conjured_mana_cake]).update_quality()

    assert conjured_mana_cake.quality == quality_before - 2
