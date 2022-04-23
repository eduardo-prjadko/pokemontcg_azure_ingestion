import os

import pytest

from pypokemontcg import PokemonTCG


@pytest.fixture(scope='session')
def pokemon_api_key():
    return os.environ.get('POKEMON_API_KEY')

@pytest.fixture(scope='session')
def container():
    return os.environ.get('CONTAINER')

@pytest.fixture(scope='session')
def prefix_path():
    return os.environ.get('PREFIX_PATH')

@pytest.fixture(scope='session')
def storage_conn_string():
    return os.environ.get('STORAGE_CONN_STRING')

@pytest.fixture(scope='session')
def cards_data(pokemon_api_key):
    pokeclient = PokemonTCG(pokemon_api_key)
    return pokeclient.cards.all().json