"""
Yemen Regions Python Library

A comprehensive Python library for accessing Yemen's administrative divisions
(governorates, districts, uzlahs, villages) with full Arabic and English support.
"""

__version__ = "1.0.0"
__author__ = "YounisDany"
__email__ = "younis@example.com"
__license__ = "MIT"

# Import main classes and enums for easy access
from .models import Governorate, District, Uzlah, Village, SearchResult
from .service import YemenRegionsService
from .enums import Language, RegionLevel

# Define what gets imported with "from yemen_regions_py import *"
__all__ = [
    "YemenRegionsService",
    "Governorate",
    "District", 
    "Uzlah",
    "Village",
    "SearchResult",
    "Language",
    "RegionLevel",
]
