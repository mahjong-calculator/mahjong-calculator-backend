from abc import ABC

from pydash.collections import group_by

from mahjong.base_handler import BaseHandler


class JapaneseMahjongHandler(BaseHandler, ABC):

    def evaluate_mahjong_hand(self, hand: list[str]):
        tiles_by_category = group_by(self._current_hand.tiles, "category")
