# pylint: disable=import-outside-toplevel
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.joinpath("src")))

import json

from fastapi.openapi.utils import get_openapi

from main import app

with open("docs/openapi.json", "w+") as fd:
    json.dump(
        get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        ),
        fd,
    )
