from fastapi import APIRouter, Depends, HTTPException, Request

from models.Function import Function 

from store import tags


from dependencies import get_token_header

router = APIRouter(
    prefix="/functions",
    tags=[tags.functions],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("", summary="Get all Functions")
async def all():
    return Function.objects.get()
 
@router.get("/{name}", summary="Get a function")
async def get(name):
    return Function.objects.get(name=name)
 

@router.post("/{name}/update", summary="Update a function")
async def update(name, request : Request):
    data = await request.json()
    return Function.objects.update(data,name=name)
 

@router.post("/create", summary="Create a new function")
async def create(request : Request):
    data = await request.json()
    return Function.objects.create(data)



@router.get("/{name}/delete", summary="Update a function")
async def delete(name):
    return Function.objects.delete(name=name)
 