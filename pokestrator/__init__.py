import logging
import os

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):

    api_key = os.environ.get('POKEMON_API_KEY')
    
    cards_info = yield context.call_activity('activity_get_cards_info', api_key)

    tasks = []
    for page in range(1, cards_info['n_of_pages'] + 1):
        tasks.append(context.call_sub_orchestrator(
            'suborch_get_cards_data',
            input_={
                'api_key': api_key,
                'page': page,
                'storage_conn_string': os.environ.get('STORAGE_CONN_STRING'),
                'container': os.environ.get('CONTAINER'),
                'prefix_path': os.environ.get('PREFIX_PATH')
            }
        ))
        
    result = yield context.task_all(tasks)

    return result

main = df.Orchestrator.create(orchestrator_function)