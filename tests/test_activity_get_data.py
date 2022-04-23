from activity_get_cards_data import main


def test_get_cards(pokemon_api_key):
    requestdata = {
        'api_key': pokemon_api_key,
        'page': 1
    }
    r = main(requestdata)

    assert r