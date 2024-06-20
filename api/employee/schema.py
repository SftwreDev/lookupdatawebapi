from datetime import datetime

from ninja import Schema


class EmployeeSchema(Schema):
    id: int
    first_name: str
    last_name: str
    urn: int
    lead_id: int
    created_at: datetime
    updated_at: datetime
    raw_json: dict
