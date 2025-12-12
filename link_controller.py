from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from typing import List

from schemas import LinkCreate, LinkResponse
from repository import Repository
from link_service import LinkService
import models
from sqlalchemy.orm import Session

router = APIRouter()

def get_repository(db: Session) -> Repository:
    return Repository(db)

@router.get("/{code}")
def redirect(
    code: str,
    service: LinkService = Depends(get_repository)
):
    url_obj = service.repository.get_original_url(code)
    if url_obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="URL not found"
        )
    return RedirectResponse(url=url_obj.address, status_code=status.HTTP_302_FOUND)

@router.get("/links", response_model=List[LinkResponse])
def get_all_links(
    service: LinkService = Depends(get_repository)
):

    try:
        return service.get_all_links()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
