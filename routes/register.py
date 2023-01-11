from fastapi import APIRouter
from models.DataBaseRequest import DataBaseRequest
from config.db import conn
import boto3
import csv
import json
from bson.json_util import dumps
from dateutil.parser import parse


register = APIRouter()

@register.post('/')
async def add_data(request: DataBaseRequest):

  client = boto3.client(
    's3',
    aws_access_key_id=request.aws_access_key_id,
    aws_secret_access_key=request.aws_secret_access_key,
  )

  obj = client.get_object(
    Bucket=request.bucket_name,
    Key=request.object_key,
  )

  data = obj['Body'].read().decode('utf-8').splitlines()

  records = csv.reader(data, delimiter=";")

  headers = next(records)

  results = []
  for row in records:
    result = {}
    for index, value in enumerate(row):
      key = headers[index]
      try:
        value = parse(value, fuzzy=False).strftime('%Y-%m-%d')
        result[key] = value
      except:
        result[key] = value
    results.append(result)
  
  conn.local.registers.insert_many(results)

  return json.loads(dumps(results))

@register.delete('/')
def delete_all():
  conn.local.registers.drop()
  return {"message": "done"}