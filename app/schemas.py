from pydantic import BaseModel, EmailStr, Field, model_validator
from uuid import UUID
from typing import Optional
from datetime import datetime

# --------------------
# User Signup Schema
# --------------------
class SignUpRequest(BaseModel):
    username: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    confirm_password: str = Field(..., min_length=6)
    agreed_to_terms: bool = Field(..., description="User must agree to terms")

    @model_validator(mode='before')  # Use 'before' so you get raw data as dict
    def passwords_match(cls, values):
        pw = values.get('password')
        cpw = values.get('confirm_password')
        if pw != cpw:
            raise ValueError('Password and Confirm Password do not match')
        return values

# --------------------
# Login Schema
# --------------------
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# --------------------
# Token Response
# --------------------
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

# For internal decoding
class TokenData(BaseModel):
    user_id: Optional[UUID] = None

# --------------------
# Forgot Password Flow
# --------------------
class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class VerifyCodeRequest(BaseModel):
    email: EmailStr
    code: str = Field(..., min_length=6, max_length=6)

class ResetPasswordRequest(BaseModel):
    email: EmailStr
    new_password: str = Field(..., min_length=6)
    code: str = Field(..., min_length=6, max_length=6)

# --------------------
# User Response
# --------------------
class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }
