import pytest
from datetime import datetime
from analyzer.reports import ReportGenerator
from analyzer.models import LogEntry


@pytest.fixture
def report_generator():
    return ReportGenerator()


@pytest.fixture
def sample_log_entries():
    return [
        LogEntry(
            timestamp=datetime(2025, 6, 22, 13, 57, 32),
            status=200,
            url="/api/context/...",
            request_method="GET",
            response_time=0.1,
            http_user_agent="test"
        ),
        LogEntry(
            timestamp=datetime(2025, 6, 22, 13, 57, 33),
            status=200,
            url="/api/context/...",
            request_method="GET",
            response_time=0.2,
            http_user_agent="test"
        ),
        LogEntry(
            timestamp=datetime(2025, 6, 22, 13, 57, 34),
            status=200,
            url="/api/homeworks/...",
            request_method="GET",
            response_time=0.3,
            http_user_agent="test"
        )
    ]


def test_generate_avg_report(report_generator, sample_log_entries):
    """Test average report generation."""
    stats = report_generator.generate_avg_report(iter(sample_log_entries))

    assert len(stats) == 2
    assert "/api/context/..." in stats
    assert "/api/homeworks/..." in stats

    context_stats = stats["/api/context/..."]
    assert context_stats.total == 2
    assert context_stats.avg_response_time == 0.15

    homeworks_stats = stats["/api/homeworks/..."]
    assert homeworks_stats.total == 1
    assert homeworks_stats.avg_response_time == 0.3


def test_generate_avg_report_with_date_filter(
    report_generator,
    sample_log_entries
):
    """Test average report generation with date filter."""
    # Add entry with different date
    different_date_entry = LogEntry(
        timestamp=datetime(2025, 6, 23, 13, 57, 32),
        status=200,
        url="/api/other/123",
        request_method="GET",
        response_time=0.5,
        http_user_agent="test"
    )

    all_entries = sample_log_entries + [different_date_entry]

    # Filter for specific date
    filter_date = datetime(2025, 6, 22)
    stats = report_generator.generate_avg_report(
        iter(all_entries),
        filter_date
    )

    # Should only include entries from 2025-06-22
    assert len(stats) == 2
    assert "/api/other" not in stats
