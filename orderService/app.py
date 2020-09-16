import json
import boto3
import logging

# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    # Some code which does something... process an invoice
    # Then create an event
    
    event_bridge = boto3.client('events')
    
    response = event_bridge.put_events(
        Entries=[
            {
                "Source": "demo.orders",
                "DetailType": "New Order",
                "Detail": json.dumps({
                    "state": "created",
                    "id": "123"
                })
            },
        ]
    )
    
    # logging.info('## RESPONSE')
    print('## RESPONSE')
    print(json.dumps(response))
    