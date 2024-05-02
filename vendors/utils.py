"""utils to use in vendors app"""

import datetime
from enum import Enum

def generate_po_number():
    """Generate PO number"""
    cur_time = datetime.datetime.now()
    po_number = str(cur_time.timestamp()).replace('.','')
    return po_number

class PoStatusEnum(Enum):
    """Enums for PO status"""
    COMPLETED = 'COMPLETED'
    PENDING = 'PENDING'
    CANCELLED = 'CANCELLED'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
