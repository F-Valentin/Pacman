import hjson
import os


class GameConfiguration:
    def __init__(self, file_path: str):
        self.file_path = file_path

        self.custom = False
        self.lives = 3
        self.level_max_time = 90

        self.points_per_pacgum = 5
        self.points_per_super_pacgum = 100
        self.points_per_ghost = 200

        self.raw_data = None

        self._load_config()

    def _load_config(self) -> None:
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Configuration file '{self.file_path}' "
                                    f"not found.")

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.raw_data = hjson.load(f)

            self.custom = bool(self.raw_data.get("custom", False))
            if self.custom is True:
                self.lives = int(self.raw_data.get("lives", 3))
                self.level_max_time = int(
                    self.raw_data.get("level_max_time", 90))
        except hjson.JSONDecodeError:
            raise ValueError("The file provided is not a valid JSON.")
        except PermissionError:
            raise PermissionError("Permission denied when accessing "
                                  "the config file.")
        except ValueError:
            raise ValueError("Configuration values type is incorect")
