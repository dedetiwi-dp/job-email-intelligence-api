# Job Email Intelligence API

AI-powered API for extracting structured information from recruiter emails.

## Features

- Extract company name
- Extract job position
- Extract salary
- Extract location
- Detect application status
- Generate summary

## Tech Stack

- Python
- FastAPI
- Ollama
- REST API

## API

POST /extract

Input:

{
  "email":"..."
}

Output:

{
  "nama_perusahaan":"",
  "posisi":"",
  "lokasi":"",
  "gaji":"",
  "status":"",
  "ringkasan":""
}
