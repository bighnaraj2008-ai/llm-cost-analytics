from datetime import datetime
from typing import Any, List, Optional

def format_currency(val: float) -> str:
    """Format float into USD currency representation."""
    return f"${val:,.4f}"

def format_tokens(n: int) -> str:
    """Format integer token count with comma thousands separators."""
    return f"{n:,}"

def parse_date(date_str: str) -> Optional[datetime]:
    """Parse date string supporting multiple standard formats."""
    formats = ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S")
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def format_table(headers: List[str], rows: List[List[Any]]) -> str:
    """Render headers and rows into clean ASCII table."""
    if not rows:
        return "No data found."
    col_widths = [len(h) for h in headers]
    for row in rows:
        for idx, val in enumerate(row):
            col_widths[idx] = max(col_widths[idx], len(str(val)))
    header_line = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    sep_line = "-+-".join("-" * col_widths[i] for i in range(len(headers)))
    row_lines = [
        " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row))
        for row in rows
    ]
    return "\n".join([header_line, sep_line] + row_lines)
