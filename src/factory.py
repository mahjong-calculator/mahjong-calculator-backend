from constants import MahjongType
from mahjong.base_handler import BaseHandler
from mahjong.japanese.factory import get_japanese_mahjong_factory
from mahjong.taiwanese.handler import TaiwaneseMahjongHandler
from schema.japanese_mahjong_schema import JapaneseMahjongSchema
from schema.taiwanese_mahjong_schema import TaiwaneseMahjongSchema


def get_mahjong_handler(mahjong_schema: JapaneseMahjongSchema | TaiwaneseMahjongSchema) -> BaseHandler:
    match mahjong_schema.mahjong_type:
        case MahjongType.JAPANESE:
            return get_japanese_mahjong_factory(mahjong_schema)
        case MahjongType.TAIWANESE:
            return TaiwaneseMahjongHandler()
        case _:
            raise ValueError("Non-supported mahjong type")
