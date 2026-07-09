from pydantic import BaseModel


class EmailRequest(BaseModel):
    subject: str
    sender: str
    body: str


class EmailResponse(BaseModel):
    company: str
    position: str
    status: str
    summary: str