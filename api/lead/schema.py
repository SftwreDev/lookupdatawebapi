from datetime import datetime

from ninja import Schema


class LeadSchema(Schema):
    id: int
    linkedin_url: str
    description: str
    n_employees: int
    urn: int
    campaign_id: int
    is_demo_lead: bool
    company_name_linkedin: str
    created_at: datetime
    updated_at: datetime
    raw_json: dict
