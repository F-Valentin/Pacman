import json
import os

class GameConfiguration:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.lives = None
        self.pacgum = None
        self.points_per_pacgum = None
        self.points_per_super_pacgum = None
        self.points_per_ghost = None
        self.seed = None
        self.level_max_time = None
        self.raw_data = None
        
        self._load_config()

    def _load_config(self) -> None:
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Configuration file '{self.file_path}' not found.")

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.raw_data = json.load(f)
            
            self.lives = self.raw_data.get("lives", "3")
            self.pacgum = self.raw_data.get("pacgum", "42")
            self.points_per_pacgum = self.raw_data.get("points_per_pacgum", "10")
            self.points_per_super_pacgum = self.raw_data.get("points_per_super_pacgum", "50")
            self.points_per_ghost = self.raw_data.get("points_per_ghost", "200")
            self.seed = self.raw_data.get("speed", "42")
            self.level_max_time = self.raw_data.get("level_max_time", "90")

        except json.JSONDecodeError:
            raise ValueError("The file provided is not a valid JSON.")
        except PermissionError:
            raise PermissionError("Permission denied when accessing the config file.")