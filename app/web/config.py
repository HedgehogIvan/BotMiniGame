from dataclasses import dataclass
from typing import Optional

import yaml
from aiohttp.web import Application


@dataclass
class Config:
    token: Optional[str] = None


def setup_config(app: Application, config_path):
    with open(config_path, 'r', encoding="utf-8") as f:
        raw_config = yaml.safe_load(f)

    app.config = Config(token=raw_config["bot"]["token"])
