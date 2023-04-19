from typing import List, Optional
from pydantic import BaseModel

class FormItem(BaseModel):
    name: Optional[str]

class FormObject(BaseModel):
    form: List[FormItem]

