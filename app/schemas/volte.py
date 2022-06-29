from typing import Union, List, Tuple

from pydantic import BaseModel


# class VocListBase(BaseModel):
#     base_ym: Union[str, None]
#     base_date: Union[str, None]
#     equip_cd0: Union[str, None]
#     pass

# class VocListInput(BaseModel):
#     start_date: str
#     end_date: str
#     belong_class: str
#     belong_nm: str
#     pass

class VolteBtsOutput(BaseModel):
    기지국명: Union[str, None]
    cut_ratio: Union[float, None]
    sum_try: Union[float, None]
    sum_suc: Union[float, None]
    sum_fail: Union[float, None]
    sum_cut: Union[float, None]
    juso: Union[str, None]
    team: Union[str, None]
    jo: Union[str, None]


class VolteTrendOutput(BaseModel):
    date: Union[str, None]
    value: Union[float, None]

#20220627 kay
class VolteEventOutput(BaseModel):
    title: Union[str, None]
    score: Union[float, None]
    rate: Union[float, None]