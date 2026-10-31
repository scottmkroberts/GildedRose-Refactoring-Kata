# -*- coding: utf-8 -*-
from __future__ import annotations

from item_names import (
    AGED_BRIE,
    BACKSTAGE_PASSES,
    CONJURED_PREFIX,
    INCREASING_QUALITY_ITEMS,
    LEGENDARY_ITEMS,
)

MIN_QUALITY = 0
MAX_QUALITY = 50
TEN_DAYS_OR_LESS = 10
FIVE_DAYS_OR_LESS = 5
NORMAL_DEGRADE_AMOUNT = 1
CONJURED_DEGRADE_AMOUNT = 2
BASE_INCREASE_AMOUNT = 1
TEN_DAYS_OR_LESS_INCREASE_AMOUNT = 2
FIVE_DAYS_OR_LESS_INCREASE_AMOUNT = 3


class GildedRose(object):
    """Manages day-to-day sell_in/quality updates for a list of Items."""

    def __init__(self, items: list[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        """Advance every item by one day, applying the shop's quality rules."""
        for item in self.items:
            if item.name in LEGENDARY_ITEMS:
                continue
            self._adjust_quality_for_today(item)
            self._decrement_sell_by_date(item)
            self._adjust_quality_if_past_due(item)

    def _adjust_quality_for_today(self, item: Item) -> None:
        """Apply today's quality change, using today's (pre-decrement) sell_in."""
        if item.name not in INCREASING_QUALITY_ITEMS:
            item.quality = max(MIN_QUALITY, item.quality - self._degrade_amount(item))
        else:
            item.quality = min(MAX_QUALITY, item.quality + self._increase_amount(item))

    def _degrade_amount(self, item: Item) -> int:
        """How much quality should degrade today for a non-appreciating item."""
        if self._is_conjured(item):
            return CONJURED_DEGRADE_AMOUNT
        return NORMAL_DEGRADE_AMOUNT

    def _increase_amount(self, item: Item) -> int:
        """How much quality should increase today for an appreciating item."""
        if item.name != BACKSTAGE_PASSES:
            return BASE_INCREASE_AMOUNT
        if item.sell_in <= FIVE_DAYS_OR_LESS:
            return FIVE_DAYS_OR_LESS_INCREASE_AMOUNT
        if item.sell_in <= TEN_DAYS_OR_LESS:
            return TEN_DAYS_OR_LESS_INCREASE_AMOUNT
        return BASE_INCREASE_AMOUNT

    def _decrement_sell_by_date(self, item: Item) -> None:
        """Age the item by one day."""
        item.sell_in -= 1

    def _adjust_quality_if_past_due(self, item: Item) -> None:
        """Apply the extra adjustment once the item's sell-by date has passed."""
        if self._is_past_sell_by_date(item):
            if item.name == AGED_BRIE:
                item.quality = min(MAX_QUALITY, item.quality + 1)
            elif item.name == BACKSTAGE_PASSES:
                item.quality = 0
            else:
                item.quality = max(
                    MIN_QUALITY, item.quality - self._degrade_amount(item)
                )

    def _is_past_sell_by_date(self, item: Item) -> bool:
        """Whether the item's sell_in has already gone negative."""
        return item.sell_in < 0

    def _is_conjured(self, item: Item) -> bool:
        """Whether the item belongs to the Conjured category (name starts with "Conjured")."""
        return item.name.startswith(CONJURED_PREFIX)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
