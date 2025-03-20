from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Any, Callable
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> ObjectId:
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object id")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler: Callable[[Any], core_schema.CoreSchema]) -> core_schema.CoreSchema:
        return core_schema.union_schema(
            [
                core_schema.is_instance_schema(ObjectId),
                core_schema.no_info_plain_validator_function(cls.validate),
            ],
            serialization=core_schema.to_string_ser_schema()
        )

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: core_schema.CoreSchema, handler: Callable[[core_schema.CoreSchema], JsonSchemaValue]) -> JsonSchemaValue:
        json_schema = handler(core_schema)
        json_schema.update(type="string")
        return json_schema

class Voter(BaseModel):
    id: str = Field(default_factory=lambda: str(PyObjectId()), alias="_id")
    name: str
    has_voted: bool = False