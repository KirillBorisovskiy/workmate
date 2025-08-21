import argparse
from datetime import datetime
from tabulate import tabulate

from analyzer.parser import LogParser
from analyzer.reports import ReportGenerator


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Log file analyzer')
    parser.add_argument(
        '--file',
        nargs='+',
        required=True,
        help='Path to log file(s)'
    )
    parser.add_argument(
        '--report',
        required=True,
        choices=['average'],
        help='Type of report to generate'
    )
    parser.add_argument('--date', help='Filter by date (YYYY-MM-DD)')

    return parser.parse_args()


def main():
    args = parse_arguments()

    date_filter = None
    if args.date:
        date_filter = datetime.strptime(args.date, '%Y-%m-%d')

    # Parse log files
    log_entries = LogParser.parse_files(args.file)

    # Generate report
    report_generator = ReportGenerator()

    if args.report == 'average':
        endpoint_stats = report_generator.generate_avg_report(
            log_entries, date_filter
        )

        # Prepare table data
        table_data = []
        for endpoint, stats in endpoint_stats.items():
            table_data.append([
                endpoint,
                stats.total,
                f"{stats.avg_response_time:.3f}"
            ])

        # Sort by request count descending
        table_data.sort(key=lambda x: x[1], reverse=True)

        # Print report
        headers = [
            "endpoint",
            "total",
            "avd-response_time"
        ]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    else:
        print(f"Report type '{args.report}' not implemented.")


if __name__ == "__main__":
    main()
