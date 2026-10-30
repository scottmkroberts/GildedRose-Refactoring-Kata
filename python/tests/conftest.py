import pytest

from gilded_rose import Item
from item_names import AGED_BRIE, BACKSTAGE_PASSES, SULFURAS


@pytest.fixture
def vest():
    return Item(name="+5 Dexterity Vest", sell_in=10, quality=20)


@pytest.fixture
def vest_at_floor():
    return Item(name="+5 Dexterity Vest", sell_in=10, quality=0)


@pytest.fixture
def vest_past_due():
    return Item(name="+5 Dexterity Vest", sell_in=0, quality=10)


@pytest.fixture
def aged_brie():
    return Item(name=AGED_BRIE, sell_in=2, quality=0)


@pytest.fixture
def aged_brie_at_cap():
    return Item(name=AGED_BRIE, sell_in=2, quality=50)


@pytest.fixture
def aged_brie_past_due():
    return Item(name=AGED_BRIE, sell_in=0, quality=10)


@pytest.fixture
def elixir():
    return Item(name="Elixir of the Mongoose", sell_in=5, quality=7)


@pytest.fixture
def elixir_past_due_near_floor():
    return Item(name="Elixir of the Mongoose", sell_in=0, quality=1)


@pytest.fixture
def sulfuras_not_yet_due():
    return Item(name=SULFURAS, sell_in=0, quality=80)


@pytest.fixture
def sulfuras_past_due():
    return Item(name=SULFURAS, sell_in=-1, quality=80)


@pytest.fixture
def backstage_pass_15_days():
    return Item(name=BACKSTAGE_PASSES, sell_in=15, quality=20)


@pytest.fixture
def backstage_pass_10_days():
    return Item(name=BACKSTAGE_PASSES, sell_in=10, quality=49)


@pytest.fixture
def backstage_pass_5_days():
    return Item(name=BACKSTAGE_PASSES, sell_in=5, quality=49)


@pytest.fixture
def backstage_pass_10_days_with_room():
    return Item(name=BACKSTAGE_PASSES, sell_in=10, quality=20)


@pytest.fixture
def backstage_pass_5_days_with_room():
    return Item(name=BACKSTAGE_PASSES, sell_in=5, quality=20)


@pytest.fixture
def backstage_pass_day_of_concert():
    return Item(name=BACKSTAGE_PASSES, sell_in=0, quality=20)


@pytest.fixture
def backstage_pass_after_concert():
    return Item(name=BACKSTAGE_PASSES, sell_in=-1, quality=0)


@pytest.fixture
def conjured_mana_cake():
    return Item(name="Conjured Mana Cake", sell_in=3, quality=6)


@pytest.fixture
def approved_items(
    vest,
    aged_brie,
    elixir,
    sulfuras_not_yet_due,
    sulfuras_past_due,
    backstage_pass_15_days,
    backstage_pass_10_days,
    backstage_pass_5_days,
    conjured_mana_cake,
):
    """Matches the item list in texttest_fixture.py / the approval baseline."""
    return [
        vest,
        aged_brie,
        elixir,
        sulfuras_not_yet_due,
        sulfuras_past_due,
        backstage_pass_15_days,
        backstage_pass_10_days,
        backstage_pass_5_days,
        conjured_mana_cake,
    ]
