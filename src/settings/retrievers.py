from pathlib import Path

from pydantic import BaseModel

from src.settings.config_reader import read_config_file


class BM25Settings(BaseModel):
    k: int
    use_gpt_preprocessor: bool


class DenseRetrieverSettings(BaseModel):
    method: str
    k: int
    threshold: float


class EnsembleRetrieverSettings(BaseModel):
    weighting: list[float]
    add_sim_ret: bool
    add_bm25_ret: bool
    add_mvec_qa_ret: bool
    add_mvec_sum_ret: bool


class RerankerSettings(BaseModel):
    k: int
    threshold: int
    batch_size: int


class MultivecSettings(BaseModel):
    k: int
    score_threshold: float


class RetrieverSettings(BaseModel):
    """Settings for the retrievers"""

    bm25: BM25Settings
    dense: DenseRetrieverSettings
    ensemble: EnsembleRetrieverSettings
    reranker: RerankerSettings
    multi_vec: MultivecSettings


yaml_path = Path("src/settings/configurations")

# Store settings from YAML configuration files in dataclasses
_cfg = read_config_file(yaml_path / "general.yaml")

RetrieverConfigs = RetrieverSettings(**_cfg.retrievers)
CFGBM25 = RetrieverConfigs.bm25
CFGDense = RetrieverConfigs.dense
CFGEns = RetrieverConfigs.ensemble
CFGRanker = RetrieverConfigs.reranker
CFGMultivec = RetrieverConfigs.multi_vec
