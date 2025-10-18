from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ...scanner.sast import scan_directory as sast_scan_directory
from ...scanner.dep_scan import scan_directory as dep_scan_directory

router = APIRouter()

class ScanRequest(BaseModel):
    directory: str

class ScanResponse(BaseModel):
    sast_issues: list
    dep_issues: list

@router.post("/", response_model=ScanResponse)
def scan_code(request: ScanRequest):
    try:
        sast_issues = sast_scan_directory(request.directory)
        dep_issues = dep_scan_directory(request.directory)
        return ScanResponse(sast_issues=sast_issues, dep_issues=dep_issues)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
