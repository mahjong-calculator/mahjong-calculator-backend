from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

from controller.get_mahjong_tiles_controller import GetMahjongTilesController
from schema.japanese_mahjong_schema import JapaneseMahjongSchema
from schema.taiwanese_mahjong_schema import TaiwaneseMahjongSchema

app = FastAPI()


@app.get("/tiles", response_model=GetMahjongTilesController.ResponseSchema)
def get_available_tiles(
    query: Annotated[JapaneseMahjongSchema | TaiwaneseMahjongSchema, Depends()]
) -> GetMahjongTilesController.ResponseSchema:
    try:
        return GetMahjongTilesController.run(query)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=exc)


@app.post("/calculate")
def calculate_mahjong_score():
    pass
