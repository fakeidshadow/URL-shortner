from fastapi import APIRouter, Depends, HTTPException, status

from schemas import LinkCreate, LinkResponse
from repository import Repository
from link_service import LinkService
import models
from sqlalchemy.orm import Session

router = APIRouter()

def get_repository(db: Session) -> Repository:
    return Repository(db)

@router.post(
    "/links",
    response_model=LinkResponse,
    status_code=status.HTTP_201_CREATED
)
def create_link(
    link_data: LinkCreate,
    service: LinkService = Depends(get_repository)
):
    status_code, result = service.create_short_link(link_data.original_url)
    
    if status_code == 201:
        url_object = service.repository.get_Url_by_id(result)
        return {
            "address": url_object.address,
            "code": url_object.code,
            "date": url_object.date
        }
    elif status_code == 208:
        existing_id = result
        existing_url = service.repository.get_Url_by_id(existing_id)
        return {
            "address": existing_url.address,
            "code": existing_url.code,
            "date": existing_url.date
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )



@router.delete("/links/{code}")
def delete_link(
    code: str,
    service: LinkService = Depends(get_repository)
):
    status_code = service.delete_link(code)
    
    if status_code == 200:
        return {
            "status": "success",
            "message": "URL deleted successfully"
        }
    elif status_code == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="URL not found"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )