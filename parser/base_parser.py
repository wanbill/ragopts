from typing import Any, Dict, List
from abc import ABC
from pathlib import Path

class BaseParser(ABC):
    def __init__(self) -> None:
        super().__init__()

    def process(self, path: Path) -> Any:
        with open(path, "r") as f:
            return f.read()

    def from_file(self, file_path: str) -> Any:
        file_path = Path(file_path)
        assert file_path.exists(), "File Not Found!"
        return self.process(file_path)

    def from_files(self, file_paths: List[str]) -> List[Any]:
        return list(map(self.from_file, file_paths))
