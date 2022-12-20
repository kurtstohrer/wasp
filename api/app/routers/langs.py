from fastapi import APIRouter, Depends, HTTPException

from models.Lang import Lang 

from store import tags


from dependencies import get_token_header

router = APIRouter(
    prefix="/langs",
    tags=[tags.langs],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("", summary="Get all Functions")
async def all():
    return Lang.objects.get()
 
@router.get("/{name}", summary="Get a single lang by name")
async def lang(name):
    return Lang.objects.get(name=name)
 

@router.get("/{name}/functions", summary="Get all Functions with this lang")
async def functions(name):
    lang = Lang.objects.get(name=name)
 
    return lang.functions()
 