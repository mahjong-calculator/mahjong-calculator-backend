from fastapi import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from constants import MahjongType
from mahjong.base_handler import BaseHandler
from mahjong.japanese.factory import get_japanese_mahjong_factory
from mahjong.taiwanese.handler import TaiwaneseMahjongHandler


def get_mahjong_handler(mahjong_type: MahjongType, mahjong_branch: str | None = None) -> BaseHandler:
    match mahjong_type:
        case MahjongType.JAPANESE:
            return get_japanese_mahjong_factory(mahjong_branch)
        case MahjongType.TAIWANESE:
            return TaiwaneseMahjongHandler()
        case _:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Non-supported mahjong type")
