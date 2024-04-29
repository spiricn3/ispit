from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Device(Base):
    __tablename__ = 'device_type'

    id=Column(Integer, primary_key=True)
    k_model=Column(String(255))
    k_methode_type=Column(String(255))
    k_calibration_metode=Column(String(255))
    k_calibration_component=Column(Integer)
    k_note=Column(String)
    k_low_level_detection=Column(Integer)
    k_max_level_detection=Column(Integer)
    k_low_negative_accepted=Column(Integer)
    

    

