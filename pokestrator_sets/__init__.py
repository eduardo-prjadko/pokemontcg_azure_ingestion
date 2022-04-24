import os

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    
    api_key = os.environ.get('POKEMON_API_KEY')

    sets_data = yield context.call_activity(
        'activity_get_sets_data', 
        {
            'api_key': api_key
        }
    )

    result = yield context.call_activity(
        'activity_upload_to_blob', 
        {
            'storage_conn_string': os.environ.get('STORAGE_CONN_STRING'),
            'container': os.environ.get('CONTAINER'),
            'prefix_path': os.environ.get('SETS_PREFIX_PATH'),
            'page': 1,
            'cards_data': sets_data
        }
    )

    return result

main = df.Orchestrator.create(orchestrator_function)