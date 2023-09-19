"""
This module contains the code to get weather data from
Visual Crossing API.
See: https://www.visualcrossing.com/
"""
from __future__ import annotations

import abc
import datetime
import json
import logging

from typing import List, Any, Dict
from urllib.request import urlopen

import aiohttp

