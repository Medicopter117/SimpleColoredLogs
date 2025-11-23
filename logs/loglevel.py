"""
Log Levels - Log-Level Definitionen
PyNum Style Naming Convention
"""

from enum import IntEnum
from colorama import Fore, Style, Back


class LogLevel(IntEnum):
    """Log-Level Definitionen"""
    TRACE = -1
    DEBUG = 0
    INFO = 1
    SUCCESS = 2
    WARN = 3
    ERROR = 4
    FATAL = 5


class LogFormat(IntEnum):
    """Output-Format Optionen"""
    SIMPLE = 0      # [LEVEL] [CATEGORY] MSG
    STANDARD = 1    # [TIMESTAMP] [LEVEL] [CATEGORY] MSG
    DETAILED = 2    # [TIMESTAMP] [LEVEL] [CATEGORY] [file.py:123] MSG
    JSON = 3        # JSON-Format für Log-Aggregation


class LevelColors:
    """Farb-Mappings für Log-Levels"""
    
    COLORS = {
        LogLevel.TRACE: Fore.LIGHTBLACK_EX,
        LogLevel.DEBUG: Fore.CYAN,
        LogLevel.INFO: Fore.WHITE,
        LogLevel.SUCCESS: Fore.GREEN,
        LogLevel.WARN: Fore.YELLOW,
        LogLevel.ERROR: Fore.RED,
        LogLevel.FATAL: Fore.WHITE + Back.RED,
    }
    
    @classmethod
    def get_color(cls, level: LogLevel) -> str:
        """Gibt die Farbe für ein Log-Level zurück"""
        return cls.COLORS.get(level, Fore.WHITE)