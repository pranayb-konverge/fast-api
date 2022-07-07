from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel



class Gender(str, Enum):
    """
    Enum class for User's Gender
    """
      
    male = "male"
    female = "female"
    
class Role(str, Enum):
    """
    Enum class for User's Role
    """
      
    admin = "admin"
    user = "user"
    student = "student"



class User(BaseModel):
    """
    Base class for users and validation of data
    """
    
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]