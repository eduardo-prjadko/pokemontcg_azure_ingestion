from pypokemontcg import PokemonTCG


def main(requestdata: dict) -> str:
    pokeclient = PokemonTCG(api_key=requestdata['api_key'])
    pokeresponse = pokeclient.sets.all()
    
    if pokeresponse.status_code != 200:
        raise Exception(f'Could not retrieve cards data from page {requestdata["page"]}.')
    else:
        return pokeresponse.json
