import json
import logging

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    
    input_ = context.get_input()

    cards_data = yield context.call_activity(
        'activity_get_cards_data', 
        {
            'api_key': input_['api_key'],
            'page': input_['page']
        }    
    )

    result = yield context.call_activity(
        'activity_upload_to_blob', 
        {
            'storage_conn_string': input_['storage_conn_string'],
            'container': input_['container'],
            'prefix_path': input_['prefix_path'],
            'page': input_['page'],
            'cards_data': cards_data
        }
    )

    return result

main = df.Orchestrator.create(orchestrator_function)