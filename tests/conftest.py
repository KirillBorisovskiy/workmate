import pytest
import tempfile
import os


@pytest.fixture
def sample_log_file():
    """Create a temporary log file with sample data."""
    log_data = [
        '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/123", "request_method": "GET", "response_time": 0.024, "http_user_agent": "test"}',
        '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/homeworks/456", "request_method": "GET", "response_time": 0.06, "http_user_agent": "test"}',
        '{"@timestamp": "2025-06-22T13:57:34+00:00", "status": 200, "url": "/api/context/789", "request_method": "GET", "response_time": 0.032, "http_user_agent": "test"}'
    ]

    with tempfile.NamedTemporaryFile(
        mode='w',
        suffix='.log',
        delete=False
    ) as f:
        for line in log_data:
            f.write(line + '\n')
        temp_file = f.name

    yield temp_file

    # Cleanup
    os.unlink(temp_file)


@pytest.fixture
def multiple_log_files():
    """Create multiple temporary log files."""
    files = []

    # First file
    data1 = [
        '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/123", "request_method": "GET", "response_time": 0.1, "http_user_agent": "test"}',
        '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/456", "request_method": "GET", "response_time": 0.2, "http_user_agent": "test"}'
    ]

    # Second file
    data2 = [
        '{"@timestamp": "2025-06-22T13:57:34+00:00", "status": 200, "url": "/api/homeworks/789", "request_method": "GET", "response_time": 0.3, "http_user_agent": "test"}',
        '{"@timestamp": "2025-06-22T13:57:34+00:00", "status": 200, "url": "/api/homeworks/101", "request_method": "GET", "response_time": 0.4, "http_user_agent": "test"}'
    ]

    for i, data in enumerate([data1, data2]):
        with tempfile.NamedTemporaryFile(
            mode='w',
            suffix=f'_{i}.log',
            delete=False
        ) as f:
            for line in data:
                f.write(line + '\n')
            files.append(f.name)

    yield files

    # Cleanup
    for file in files:
        os.unlink(file)
