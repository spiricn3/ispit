from pydantic import BaseModel
from typing import Optional


class MyDevice(BaseModel):
    id: int 
    k_model: Optional [str]
    k_methode_type:Optional [str]
    k_calibration_metode:Optional [str]
    k_calibration_component:Optional [int]
    k_note:Optional [str]
    k_low_level_detection:Optional [int]
    k_max_level_detection:Optional [int]
    k_low_negative_accepted:Optional [int]
