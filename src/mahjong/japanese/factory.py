from mahjong.japanese.branch.normal_mahjong_handler import NormalJapaneseMahjongHandler
from mahjong.japanese.branch.three_player_mahjong_handler import ThreePlayerJapaneseMahjongHandler
from mahjong.japanese.constants import JapaneseMahjongBranch
from schema.japanese_mahjong_schema import JapaneseMahjongSchema


def get_japanese_mahjong_factory(mahjong_schema: JapaneseMahjongSchema):
    japanese_mahjong_branch: JapaneseMahjongBranch = mahjong_schema.mahjong_branch
    if japanese_mahjong_branch == JapaneseMahjongBranch.NORMAL:
        return NormalJapaneseMahjongHandler()
    elif japanese_mahjong_branch == JapaneseMahjongBranch.THREE_PLAYER:
        return ThreePlayerJapaneseMahjongHandler()
    else:
        raise ValueError("Non-supported japanese mahjong type")
