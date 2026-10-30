import pytest

from gilded_rose import Item


@pytest.fixture
def vest():
    return Item(name="+5 Dexterity Vest", sell_in=10, quality=20)


@pytest.fixture
def vest_at_floor():
    return Item(name="+5 Dexterity Vest", sell_in=10, quality=0)


@pytest.fixture
def aged_brie():
    return Item(name="Aged Brie", sell_in=2, quality=0)


@pytest.fixture
def aged_brie_at_cap():
    return Item(name="Aged Brie", sell_in=2, quality=50)


@pytest.fixture
def elixir():
    return Item(name="Elixir of the Mongoose", sell_in=5, quality=7)


@pytest.fixture
def elixir_past_due_near_floor():
    return Item(name="Elixir of the Mongoose", sell_in=0, quality=1)


@pytest.fixture
def sulfuras_not_yet_due():
    return Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)


@pytest.fixture
def sulfuras_past_due():
    return Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)


@pytest.fixture
def backstage_pass_15_days():
    return Item(
        name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20
    )


@pytest.fixture
def backstage_pass_10_days():
    return Item(
        name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49
    )


@pytest.fixture
def backstage_pass_5_days():
    return Item(
        name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49
    )


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
