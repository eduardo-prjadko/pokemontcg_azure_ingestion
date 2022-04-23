from datetime import datetime
import json
import logging

from azure.storage.blob import BlobServiceClient


def main(uploadsettings: dict) -> str:
    blob_service_client = BlobServiceClient \
        .from_connection_string(uploadsettings['storage_conn_string'])
    
    today = datetime.today().date()
    blob_name = f'cards_{today.strftime("%Y%m%d")}_{uploadsettings["page"]:03}.json'
    blob_path = f'{uploadsettings["prefix_path"]}/{today.year}/' \
        f'{today.month:02}/{today.day:02}'
    blob_client = blob_service_client.get_blob_client(
        container=uploadsettings['container'],
        blob=f'{blob_path}/{blob_name}'
    )
    upload_return = blob_client.upload_blob(
        data=json.dumps(uploadsettings['cards_data']),
        overwrite=True
    )

    result = {
        'blob_path': blob_path,
        'blob_name': blob_name
    }
    
    return result