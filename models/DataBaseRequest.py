from pydantic import BaseModel


class DataBaseRequest(BaseModel):
  bucket_name: str
  object_key: str
  aws_access_key_id: str
  aws_secret_access_key: str