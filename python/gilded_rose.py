# -*- coding: utf-8 -*-
from __future__ import annotations

from item_names import AGED_BRIE, BACKSTAGE_PASSES, SULFURAS


class GildedRose(object):
    """Manages day-to-day sell_in/quality updates for a list of Items."""

    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        """Advance every item by one day, applying the shop's quality rules."""
        for item in self.items:
            if item.name == SULFURAS:
                continue
            self._adjust_quality_for_today(item)
            self._advance_sell_in(item)
            self._adjust_quality_if_past_due(item)

    def _adjust_quality_for_today(self, item: Item) -> None:
        """Apply today's quality change, using today's (pre-decrement) sell_in."""
        if item.name != AGED_BRIE and item.name != BACKSTAGE_PASSES:
            if item.quality > 0:
                item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == BACKSTAGE_PASSES:
                    if item.sell_in < 11 and item.quality < 50:
                        item.quality = item.quality + 1
                    if item.sell_in < 6 and item.quality < 50:
                        item.quality = item.quality + 1

    def _advance_sell_in(self, item: Item) -> None:
        """Age the item by one day."""
        item.sell_in = item.sell_in - 1

    def _adjust_quality_if_past_due(self, item: Item) -> None:
        """Apply the extra adjustment once the item's sell-by date has passed."""
        if item.sell_in < 0:
            if item.name != AGED_BRIE:
                if item.name != BACKSTAGE_PASSES:
                    if item.quality > 0:
                        item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
