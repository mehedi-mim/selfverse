import datetime
import pytz
from sqlalchemy import Boolean, Column, Integer, String, DateTime, event


class CommonBase:
    """Contains common field usable by all models"""
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.now(tz=pytz.timezone('UTC')), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.datetime.now(tz=pytz.timezone('UTC')), nullable=False,
        onupdate=datetime.datetime.now(tz=pytz.timezone('UTC'))
    )
