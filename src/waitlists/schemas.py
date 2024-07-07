from datetime import datetime
from ninja import Schema


class WaitlistEntryCreateSchema(Schema):
    email: str


class WaitlistEntryDetailSchema(Schema):
    email: str
    timestamp: datetime
