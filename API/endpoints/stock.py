from fastapi import APIRouter, Request, Response, HTTPException, status
from ..models import models
from ..helpers import helpers

router = APIRouter(
    prefix="/stock",
    tags=["stock"],
)


@router.put("/category")
async def create_category(category: models.StockCategory, req: Request, res: Response):
    user = helpers.verify_token(req.headers["authorization"].split("Bearer ")[1])
    category_dict = {
        "user": user["_id"],
        "name": category.name,
        "type": category.type
    }
    exists = helpers.database["categories"].find_one(category_dict)
    if exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Category Already Exists",
        )
    helpers.database["categories"].insert_one(category_dict)
    res.status_code = 201
    return {"status": 201, "message": "category created successfully"}


@router.delete("/category")
async def delete_category(category: models.StockCategory, req: Request, res: Response):
    pass


@router.get("/category")
async def get_category(req: Request):
    user = helpers.verify_token(req.headers["authorization"].split("Bearer ")[1])
    categories = helpers.database["categories"].find({"user": user["_id"]})
    categories = [{"name": category["name"], "type": category["type"]} for category in categories]
    return {"status": 200, "content": categories}
