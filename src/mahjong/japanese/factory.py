from fastapi import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from mahjong.japanese.branch.four_player_mahjong_handler import FourPlayerJapaneseMahjongHandler
from mahjong.japanese.branch.three_player_mahjong_handler import ThreePlayerJapaneseMahjongHandler
from mahjong.japanese.constants import JapaneseMahjongBranch


def get_japanese_mahjong_factory(mahjong_branch: str):
    try:
        japanese_mahjong_branch = JapaneseMahjongBranch(mahjong_branch)
        match japanese_mahjong_branch:
            case JapaneseMahjongBranch.FOUR_PLAYER:
                return FourPlayerJapaneseMahjongHandler()
            case JapaneseMahjongBranch.THREE_PLAYER:
                return ThreePlayerJapaneseMahjongHandler()
    except Exception as exc:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Non-supported japanese mahjong branch."
        ) from exc
