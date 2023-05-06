from typing import List, Optional
from pydantic import BaseModel

class FormItem(BaseModel):
    label: Optional[str]
    type: Optional[str]
    value: Optional[str]  

