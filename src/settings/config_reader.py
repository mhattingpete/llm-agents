from pathlib import Path

from omegaconf import DictConfig, OmegaConf


def read_config_file(file_path: str) -> DictConfig:
    """Loads a YAML file

    Args:
        file_path (str): A file path as string

    Returns:
        dict: Returns an Omegaconf dict of configurations
    """
    cfg = OmegaConf.load(Path(file_path))
    return cfg
