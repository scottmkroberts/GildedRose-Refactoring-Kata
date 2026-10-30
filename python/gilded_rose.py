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
            if item.name != AGED_BRIE and item.name != BACKSTAGE_PASSES:
                if item.quality > 0:
                    if item.name != SULFURAS:
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == BACKSTAGE_PASSES:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != AGED_BRIE:
                    if item.name != BACKSTAGE_PASSES:
                        if item.quality > 0:
                            if item.name != SULFURAS:
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
