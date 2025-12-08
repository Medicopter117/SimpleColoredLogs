# __init__.py

# Exponiert alle Hauptkomponenten aus logger.py
from .logger import (
    logger, 
    LogLevel, 
    LogFormat,
    Category,
    C # NEU: Die hierarchische Kategorie-Zugriffsklasse
)

# Optional: Setzt die Haupt-Logger-Klasse als Standard-Import
__all__ = [
    "logger", 
    "LogLevel", 
    "LogFormat",
    "Category",
    "C"
]