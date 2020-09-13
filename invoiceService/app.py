import json
import boto3

def lambda_handler(event, context):
    
    # Event contains the order info
    # Does some work to create an Invoice
    
    print('## EVENT')
    print(event)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "invoiceOrder Function",
        }),
    }
