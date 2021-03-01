import re
import json
import boto3
from botocore.exceptions import ClientError

def get_all(_event, _context):
    client = boto3.resource("dynamodb")
    table = client.Table("EestiKott")
    sentences = table.scan()
    print(sentences)
    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda!")
    }

# "?" and "!" should be remained,,,better in front?
# def capitalize_first_latters(text):
#     new = re.split(r' *[\.\?!][\'"\)\]]* *', text)
#     return [item.capitalize() for item in new]

def insert_item(event, _context):
    client = boto3.resource("dynamodb")
    table = client.Table("EestiKott")

    new_text = event["new_sentence"]
    new_sentence = capitalize_first_latters(new_text)
    new_text = event["new_eesti"]
    new_eesti = capitalize_first_latters(new_text)

    try:
        table.put_item(
            Item={
                "SentenceID": new_sentence,
                "Eesti": new_eesti
            }
        )
        return {
            "statusCode": 200,
            "body": json.dumps("New data inserted!")
        }
    except ClientError as e:
        return {
            "statusCode": 400,
            "body": json.dumps(e.response['Error']['Message'])
        }




