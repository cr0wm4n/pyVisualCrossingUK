"""Python Wrapper for Visual Crossing Weather API."""
from __future__ import annotations

from pyVisualCrossing.api import (
    VisualCrossing,
    VisualCrossingBadRequest,
    VisualCrossingInternalServerError,
    VisualCrossingTooManyRequests,
    VisualCrossingUnauthorized,
)
from pyVisualCrossing.data import ForecastData, ForecastDailyData, ForecastHourlyData

__title__ = "pyVisualCrossing"
__version__ = "0.1.7"
__author__ = "briis"
__license__ = "MIT"
