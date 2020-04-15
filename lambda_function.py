import json
import boto3
import random
from botocore.exceptions import ClientError

region_session = boto3.Session(region_name='us-east-1')
dynamodb = region_session.resource('dynamodb')
table = dynamodb.Table("prototype_vscode")


def lambda_handler(event, context):
    method = event["requestContext"]["httpMethod"]
    try:
        if method == 'POST':
            data = json.loads(event["body"])
            html_component = data["generated_webpage_html"]
            css_component = data["generated_webpage_css"]
            id = ''.join(random.choice('0123456789') for _ in range(6))
            item = {
                "id": id,
                "generated_webpage_html": html_component,
                "generated_webpage_css": css_component
            }
            dynamodb_reponse = table.put_item(Item=item)
            status_code = dynamodb_reponse["ResponseMetadata"]["HTTPStatusCode"]
            body = {'id': id} if status_code == 200 else f'Unknown Error Occured'
        elif method == 'GET':
            id = event["pathParameters"]["id"]
            dynamodb_reponse = table.get_item(Key={'id': id})
            status_code = dynamodb_reponse["ResponseMetadata"]["HTTPStatusCode"]
            if status_code == 200:
                item = dynamodb_reponse.get("Item", None)
                if item:
                    body = item
                else:
                    status_code = 404
                    body = f'No HTML & CSS Code Exist for {id}'
    except ValueError as e:
        raise e

    return {
        'statusCode': status_code,
        'body': json.dumps(body),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        'isBase64Encoded': False,
    }