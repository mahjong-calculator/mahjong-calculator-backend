from typing import Any

import pytest
from fastapi.testclient import TestClient
from httpx import Response
from starlette.status import HTTP_200_OK, HTTP_422_UNPROCESSABLE_ENTITY


class TestGetMahjongTilesController:

    @pytest.fixture(autouse=True)
    def apply_client(self, mock_client: TestClient):
        self.client = mock_client  # pylint: disable=attribute-defined-outside-init

    def trigger_run(self, params: dict[str, Any]) -> Response:
        return self.client.get("/tiles", params=params)

    def test_japanese_mahjong_normal(self):
        params = {"mahjong_type": "japanese", "mahjong_branch": "four_player"}
        res = self.trigger_run(params)

        assert res.status_code == HTTP_200_OK
        assert res.json() == {
            "mahjong_type": "japanese",
            "mahjong_branch": "four_player",
            "tiles": {
                "1m": 4,
                "2m": 4,
                "3m": 4,
                "4m": 4,
                "5m": 3,
                "5md": 1,
                "6m": 4,
                "7m": 4,
                "8m": 4,
                "9m": 4,
                "1p": 4,
                "2p": 4,
                "3p": 4,
                "4p": 4,
                "5p": 3,
                "5pd": 1,
                "6p": 4,
                "7p": 4,
                "8p": 4,
                "9p": 4,
                "1s": 4,
                "2s": 4,
                "3s": 4,
                "4s": 4,
                "5s": 3,
                "5sd": 1,
                "6s": 4,
                "7s": 4,
                "8s": 4,
                "9s": 4,
                "E": 4,
                "S": 4,
                "W": 4,
                "N": 4,
                "R": 4,
                "G": 4,
                "B": 4,
            },
        }

    def test_japanese_mahjong_three_player(self):
        params = {"mahjong_type": "japanese", "mahjong_branch": "three_player"}
        res = self.trigger_run(params)

        assert res.status_code == HTTP_200_OK
        assert res.json() == {
            "mahjong_type": "japanese",
            "mahjong_branch": "three_player",
            "tiles": {
                "1m": 4,
                "9m": 4,
                "1p": 4,
                "2p": 4,
                "3p": 4,
                "4p": 4,
                "5p": 3,
                "5pd": 1,
                "6p": 4,
                "7p": 4,
                "8p": 4,
                "9p": 4,
                "1s": 4,
                "2s": 4,
                "3s": 4,
                "4s": 4,
                "5s": 3,
                "5sd": 1,
                "6s": 4,
                "7s": 4,
                "8s": 4,
                "9s": 4,
                "E": 4,
                "S": 4,
                "W": 4,
                "N": 4,
                "R": 4,
                "G": 4,
                "B": 4,
            },
        }

    def test_japanese_mahjong_wrong_branch(self):
        params = {"mahjong_type": "japanese", "mahjong_branch": "wrong_branch"}
        res = self.trigger_run(params)

        assert res.status_code == HTTP_422_UNPROCESSABLE_ENTITY

    def test_taiwanese_mahjong(self):
        params = {"mahjong_type": "taiwanese"}
        res = self.trigger_run(params)

        assert res.status_code == HTTP_200_OK
        assert res.json() == {
            "mahjong_type": "taiwanese",
            "mahjong_branch": None,
            "tiles": {
                "1m": 4,
                "2m": 4,
                "3m": 4,
                "4m": 4,
                "5m": 4,
                "6m": 4,
                "7m": 4,
                "8m": 4,
                "9m": 4,
                "1p": 4,
                "2p": 4,
                "3p": 4,
                "4p": 4,
                "5p": 4,
                "6p": 4,
                "7p": 4,
                "8p": 4,
                "9p": 4,
                "1s": 4,
                "2s": 4,
                "3s": 4,
                "4s": 4,
                "5s": 4,
                "6s": 4,
                "7s": 4,
                "8s": 4,
                "9s": 4,
                "E": 4,
                "S": 4,
                "W": 4,
                "N": 4,
                "R": 4,
                "G": 4,
                "B": 4,
                "Pl": 1,
                "Or": 1,
                "Ba": 1,
                "Ch": 1,
                "Sp": 1,
                "Su": 1,
                "Au": 1,
                "Wi": 1,
            },
        }

    def test_wrong_type(self):
        params = {"mahjong_type": "wrong_type"}
        res = self.trigger_run(params)

        assert res.status_code == HTTP_422_UNPROCESSABLE_ENTITY
