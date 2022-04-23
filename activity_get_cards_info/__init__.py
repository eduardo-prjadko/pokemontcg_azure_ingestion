import logging

from pypokemontcg import PokemonTCG


def main(apikey: str) -> dict:
    pokeclient = PokemonTCG(api_key=apikey)
    pokeresponse = pokeclient.cards.all()

    if pokeresponse.status_code != 200:
        raise Exception('Could not retrieve cards call information.')
    else:
        return {'n_of_pages': pokeresponse.pages}
