from activity_get_sets_data import main


def test_activity_get_sets_data(pokemon_api_key):
    r = main({'api_key': pokemon_api_key})

    assert r