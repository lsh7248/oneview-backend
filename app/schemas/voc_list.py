from typing import Union, List, Tuple

from pydantic import BaseModel


class VocListBase(BaseModel):
    base_ym: Union[str, None]
    base_date: Union[str, None]
    equip_cd0: Union[str, None]
    pass

class VocListInput(BaseModel):
    start_date: str
    end_date: str
    belong_class: str
    belong_nm: str
    pass

class VocListOutput(VocListBase):
    pass

