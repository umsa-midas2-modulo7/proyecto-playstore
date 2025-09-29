from typing import TypedDict

class AppInfo(TypedDict):
    app_id: str
    name: str

from dataclasses import dataclass

@dataclass
class App:
    app_id: str
    name: str
    
    def __post_init__(self):
        if not self.app_id:
            raise ValueError("app_id no puede estar vacío")