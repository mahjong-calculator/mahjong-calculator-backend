from typing import Annotated

from fastapi import Depends, FastAPI

from controller.get_mahjong_tiles_controller import GetMahjongTilesController

app = FastAPI()


@app.get("/tiles", response_model=GetMahjongTilesController.ResponseSchema)
def get_available_tiles(
    query: Annotated[GetMahjongTilesController.RequestQuerySchema, Depends()]
) -> GetMahjongTilesController.ResponseSchema:
    return GetMahjongTilesController.run(query)


@app.post("/calculate")
def calculate_mahjong_score():
    pass
