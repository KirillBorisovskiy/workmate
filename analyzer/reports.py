from typing import Dict, Iterator, Optional
from datetime import datetime
from .models import EndpointStats


class ReportGenerator:
    def generate_avg_report(
        self,
        log_entries: Iterator,
        date_filter: Optional[datetime] = None
    ) -> Dict[str, EndpointStats]:
        """Generate average response time report by endpoint."""
        endpoint_stats: Dict[str, EndpointStats] = {}

        for entry in log_entries:
            if date_filter and entry.timestamp.date() != date_filter.date():
                continue

            endpoint = entry.url

            if endpoint not in endpoint_stats:
                endpoint_stats[endpoint] = EndpointStats(
                    endpoint=endpoint,
                    total=0,
                    avg_response_time=0.0,
                    total_response_time=0.0
                )

            endpoint_stats[endpoint].add_response_time(entry.response_time)

        return endpoint_stats
