from pydantic import RootModel

from controller.base import BaseController
from factory import get_mahjong_handler
from schema.japanese_mahjong_schema import JapaneseMahjongSchema
from schema.taiwanese_mahjong_schema import TaiwaneseMahjongSchema


class GetMahjongTilesController(BaseController):

    class ResponseSchema(RootModel):
        root: list[str]

    @classmethod
    def run(cls, query: JapaneseMahjongSchema | TaiwaneseMahjongSchema) -> ResponseSchema:
        handler = get_mahjong_handler(query)
        tiles = handler.get_available_tiles()

        return cls.ResponseSchema(root=[tile.abbreviation for tile in tiles])
