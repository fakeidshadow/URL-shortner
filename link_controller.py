from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from typing import List

from schemas import LinkCreate, LinkResponse
from repository import Repository
from link_service import LinkService
import models
from sqlalchemy.orm import Session
from schemas import LinkResponse
import repository

router = APIRouter()


def get_repository(db: Session = Depends(lambda: repository.session)) -> LinkService:
    repo = Repository(db)
    return LinkService(repo)


@router.get("/{code}")
def redirect(
        code: str,
        service: LinkService = Depends(get_repository)
) -> RedirectResponse:
    url_obj = service.get_original_url(code)
    if url_obj[0] == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="URL not found"
        )
    return RedirectResponse(url=url_obj[1], status_code=status.HTTP_302_FOUND)


@router.get("/all/links")
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


@router.post(
    "/links",
    response_model=LinkResponse,
    status_code=status.HTTP_201_CREATED
)
def create_link(
        link_data: LinkCreate,
        service: LinkService = Depends(get_repository)
):
    ans = service.create_short_link(link_data.address)

    if ans[0] == 201:
        url_object = service.repository.get_Url_by_id(ans[1])
        return {
            "address": url_object.address,
            "code": url_object.code,
            "date": url_object.date
        }
    elif ans[0] == 208:
        existing_id = ans[1]
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