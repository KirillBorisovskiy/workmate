import json
from typing import Iterator, List
from .models import LogEntry


class LogParser:
    @staticmethod
    def parse_file(file_path: str) -> Iterator[LogEntry]:
        """Parse log file and yield LogEntry objects."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        data = json.loads(line)
                        yield LogEntry.from_dict(data)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error reading file {file_path}: {e}")

    @staticmethod
    def parse_files(file_paths: List[str]) -> Iterator[LogEntry]:
        """Parse multiple log files."""
        for file_path in file_paths:
            yield from LogParser.parse_file(file_path)
