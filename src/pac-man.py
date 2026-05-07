import sys
from parsing import GameConfiguration


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 pac-man.py <config.json>")
        return

    file_path = sys.argv[1]

    try:
        config = GameConfiguration(file_path)
        print(f"Game Configuration loaded (custom:{config.custom})")

    except (FileNotFoundError, ValueError, PermissionError) as e:
        print(f"Configuration Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
