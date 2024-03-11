from pathlib import Path

from pydantic import BaseModel, Field, computed_field

from src.settings.config_reader import read_config_file


class BaseSettings(BaseModel):
    """Settings for the chat model"""

    # required fields
    name: str = Field(
        description="Name of the model being used, this is the model langchain will use."
    )
    temperature: float = Field(ge=0, le=1, description="Temperature of model")

    # optional fields
    max_tokens: int = Field(default=500, description="Max tokens of model")
    streaming: bool = Field(default=True, description="Enable streaming")
    top_k: int = Field(default=50, description="Top k of model")
    repetition_penalty: float = Field(
        default=1.03, description="Repetition penalty of model"
    )
    stop_sequences: list[str] = Field(
        default=["\nNew input", "\nObservation"],
        description="List of sequences to stop the model generation at.",
    )


class HFBaseSettings(BaseSettings):
    """Settings for HF chat models"""

    # optional fields
    task: str = Field(
        default="text-generation", description="Hugging face task the model is for."
    )

    @computed_field
    @property
    def endpoint_url(self) -> str:
        return f"https://api-inference.huggingface.co/models/{self.name}"


class OpenChatSettings(HFBaseSettings):
    """Openchat settings"""

    name: str = "openchat/openchat-3.5-0106"


class EmbeddingModelSettings(BaseModel):
    """Settings for the embedding model"""

    deployment_name: str = "text-embedding-ada-002"
    name: str = "text-embedding-ada-002"
    batch_size: int = Field(default=1, description="Chunks to process in parallel")


yaml_path = Path("src/settings/configurations")

_cfg = read_config_file(yaml_path / "models.yaml")

# Store model settings object
CFGHFOpenchat = OpenChatSettings(**_cfg.openchat35)
