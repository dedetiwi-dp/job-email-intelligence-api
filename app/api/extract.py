import json
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ollama_service import chat

router = APIRouter()

class EmailRequest(BaseModel):
    email: str

@router.post("/extract")
def extract(request: EmailRequest):

    email = request.email

    prompt = f"""
    Kamu adalah AI yang mengekstrak informasi email recruiter.

    Analisa email berikut.

    Ekstrak informasi:

    - nama_perusahaan
    - posisi
    - lokasi
    - gaji
    - link
    - status
    - ringkasan

    Aturan:

    1. status hanya boleh salah satu:
    - Applied
    - Interview
    - Offer
    - Rejected
    - Other

    2. ringkasan maksimal 2 kalimat.

    3. Jangan menerjemahkan isi email.

    4. Gunakan informasi yang benar-benar ada pada email.

    5. Jika tidak ada isi suatu field isi dengan string kosong "".

    Email:

    {email}

    Jawab JSON saja.

    {{
    "nama_perusahaan":"",
    "posisi":"",
    "lokasi":"",
    "gaji":"",
    "link":"",
    "status":"",
    "ringkasan":""
    }}
    """

    hasil = chat(prompt)

    awal = hasil.find("{")
    akhir = hasil.rfind("}") + 1

    json_text = hasil[awal:akhir]

    data = json.loads(json_text)

    return data