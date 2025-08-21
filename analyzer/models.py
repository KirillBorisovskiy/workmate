from dataclasses import dataclass
from datetime import datetime
from typing import Dict


@dataclass
class LogEntry:
    timestamp: datetime
    status: int
    url: str
    request_method: str
    response_time: float
    http_user_agent: str

    @classmethod
    def from_dict(cls, data: Dict) -> 'LogEntry':
        return cls(
            timestamp=datetime.fromisoformat(data['@timestamp']),
            status=data['status'],
            url=data['url'],
            request_method=data['request_method'],
            response_time=data['response_time'],
            http_user_agent=data['http_user_agent']
        )


@dataclass
class EndpointStats:
    endpoint: str
    total: int
    avg_response_time: float
    total_response_time: float

    def add_response_time(self, response_time: float):
        self.total_response_time += response_time
        self.total += 1
        self.avg_response_time = round(
            self.total_response_time / self.total,
            3
        )
