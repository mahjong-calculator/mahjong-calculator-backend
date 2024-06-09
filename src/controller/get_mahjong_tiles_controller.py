from pydantic import BaseModel, Field

from constants import MahjongType
from controller.base import BaseController
from factory import get_mahjong_handler


class GetMahjongTilesController(BaseController):
    class RequestQuerySchema(BaseModel):
        mahjong_type: MahjongType = Field(title="Mahjong Type", examples=[MahjongType.JAPANESE, MahjongType.TAIWANESE])
        mahjong_branch: str | None = Field(None, title="Mahjong Branch", examples=["four_player", "three_player"])

    class ResponseSchema(BaseModel):
        mahjong_type: MahjongType = Field(title="Mahjong Type", examples=[MahjongType.JAPANESE, MahjongType.TAIWANESE])
        mahjong_branch: str | None = Field(None, title="Mahjong Branch", examples=["four_player", "three_player"])
        tiles: dict[str, int] = Field(title="Available Tiles", examples=[{"1m": 4, "9m": 4}])

    @classmethod
    def run(cls, query: RequestQuerySchema) -> ResponseSchema:
        handler = get_mahjong_handler(query.mahjong_type, query.mahjong_branch)
        tiles = handler.get_available_tiles_abbreviation_and_number()

        return cls.ResponseSchema(mahjong_type=query.mahjong_type, mahjong_branch=query.mahjong_branch, tiles=tiles)
