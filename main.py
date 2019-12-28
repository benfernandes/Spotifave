from pathlib import Path

from spotifave.config import Config


def main(config_file_path: Path):
    config = Config(config_file_path)


if __name__ == '__main__':
    main(
        Path('../appConfig.json')
    )
