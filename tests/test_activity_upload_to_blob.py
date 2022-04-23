import logging

from azure.storage.blob import BlobServiceClient

from activity_upload_to_blob import main


def test_activity_upload_to_blob(
    container: str,
    prefix_path: str,
    storage_conn_string: str,
    cards_data: dict
):
    uploadsettings = {
        'storage_conn_string': storage_conn_string,
        'container': container,
        'prefix_path': prefix_path,
        'cards_data': cards_data,
        'page': 1
    }

    r = main(uploadsettings)

    logging.debug(f'upload result: {r}')

    assert r

    blob_service_client = BlobServiceClient \
        .from_connection_string(storage_conn_string)
    blob_client = blob_service_client.get_blob_client(
        container=container,
        blob=f'{r["blob_path"]}/{r["blob_name"]}'
    )
    blob_client.delete_blob()