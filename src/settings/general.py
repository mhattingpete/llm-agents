from pathlib import Path

from pydantic import BaseModel

from src.settings.config_reader import read_config_file


class ModelTypeSettings(BaseModel):
    type: str


yaml_path = Path("src/settings/configurations")

# Store settings from YAML configuration files in dataclasses
_cfg = read_config_file(yaml_path / "general.yaml")

CFGModelType = ModelTypeSettings(**_cfg.models)
