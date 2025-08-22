import pytest
from analyzer.parser import LogParser
from analyzer.models import LogEntry


def test_parse_file(sample_log_file):
    """Test parsing a single log file."""
    entries = list(LogParser.parse_file(sample_log_file))

    assert len(entries) == 3
    assert all(isinstance(entry, LogEntry) for entry in entries)
    assert entries[0].url == "/api/context/..."
    assert entries[0].response_time == 0.024
    assert entries[0].status == 200


def test_parse_multiple_files(multiple_log_files):
    """Test parsing multiple log files."""
    entries = list(LogParser.parse_files(multiple_log_files))

    assert len(entries) == 4
    assert all(isinstance(entry, LogEntry) for entry in entries)


def test_parse_nonexistent_file():
    """Test parsing a non-existent file."""
    with pytest.raises(FileNotFoundError):
        list(LogParser.parse_file("nonexistent.log"))


def test_parse_invalid_json(tmp_path):
    """Test parsing file with invalid JSON."""
    invalid_file = tmp_path / "invalid.log"
    invalid_file.write_text('{"invalid": json\n')

    with pytest.raises(Exception):
        list(LogParser.parse_file(str(invalid_file)))
