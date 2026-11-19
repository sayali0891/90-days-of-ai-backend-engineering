from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id : int
    # account_id: int = Field(gt=0)

    # custom valdator
    @field_validator("account_id")
    def validate_account_id(cls, value):    # @field_validator behaves like a Class Method (@classmethod). This means its very first argument must always be the class itself (usually named cls), followed by the value you want to validate.
        if(value <= 0):
            raise ValueError(f"account_id must be a positive value : {value}")
        return value

user = User(name="Sayali", email="sayali@gmail.com", account_id=1234)
print(user)


# Another use of Pydantic is JSON Serialization : Converts the data from llm into json format
"""
1. user_json_str = user.json()
2. user_json_str = user.dict()
3. user = User.parse_raw(json_str)
"""

