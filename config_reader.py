from dataclasses import dataclass
from pathlib import Path
from typing import Union

import toml

FILE_PATH = Path(__file__).with_name("config.toml")


@dataclass(frozen=True)
class Config:
    ENCRYPTION_ALGORITHM: str
    MAX_CHUNK_REPLICA: int

    @classmethod
    def from_file(cls, filepath: Union[Path, str] = FILE_PATH) -> "Config":
        with open(filepath, "r", encoding="utf-8") as f:
            raw_config = toml.load(f).get("config", {})

        return cls(
            ENCRYPTION_ALGORITHM=raw_config.get("ENCRYPTION_ALGORITHM", ""),
            MAX_CHUNK_REPLICA=int(raw_config.get("MAX_CHUNK_REPLICA", 0)),
        )

    @classmethod
    def load(cls, filepath: Union[Path, str] = FILE_PATH) -> "Config":
        return cls.from_file(filepath)


CONFIG = Config.load()


def load_config(filepath: Union[Path, str] = FILE_PATH):
    with open(filepath, "r", encoding="utf-8") as f:
        return toml.load(f)["config"]
