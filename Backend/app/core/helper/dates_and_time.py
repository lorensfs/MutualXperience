from datetime import datetime, timedelta
from typing import Literal, Optional, Tuple

timedelta_units = Literal[
    "microseconds", "milliseconds", "seconds", "minutes", "hours", "days", "weeks"
]


def adjust_date(base: datetime, delta: float, unit: timedelta_units) -> datetime:
    if delta == 0:
        return base
    elif delta > 0:
        return base + timedelta(**{unit: delta})
    elif delta < 0:
        return base - timedelta(**{unit: abs(delta)})


def process_dates(
    *,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    start_delta: float = -7,
    end_delta: float = 0,
    start_unit: timedelta_units = "days",
    end_unit: timedelta_units = "days",
) -> Tuple[float, float]:
    end_date = end_date or datetime.now()

    if start_date is None:
        start_date = adjust_date(datetime.now(), start_delta, start_unit)

    if end_date is None:
        end_date = adjust_date(datetime.now(), end_delta, end_unit)

    return start_date.timestamp(), end_date.timestamp()
