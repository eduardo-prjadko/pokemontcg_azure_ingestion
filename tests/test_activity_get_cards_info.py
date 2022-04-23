import logging

from activity_get_cards_info import main


def test_get_cards(pokemon_api_key):
    r = main(pokemon_api_key)

    assert r