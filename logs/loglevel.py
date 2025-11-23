"""
Log Levels - Log-Level Definitionen
PyNum Style Naming Convention
"""

from enum import IntEnum
from colorama import Fore, Style, Back


class LogLevel(IntEnum):
    """Log-Level Definitionen"""
    TRACE = -1      # Sehr detaillierte Debug-Infos
    DEBUG = 0       # Entwickler-Informationen
    INFO = 1        # Allgemeine Informationen
    SUCCESS = 2     # Erfolgreiche Operationen
    LOADING = 3     # Startet Lade-Vorgang
    PROCESSING = 4  # Verarbeitet gerade
    PROGRESS = 5    # Fortschritts-Update (z.B. 45%)
    WAITING = 6     # Wartet auf Ressource/Response
    NOTICE = 7      # Wichtige Hinweise (zwischen INFO und WARN)
    WARN = 8        # Warnungen
    ERROR = 9       # Fehler
    CRITICAL = 10   # Kritische Fehler (noch behebbar)
    FATAL = 11      # Fatale Fehler (Programm-Absturz)
    SECURITY = 12   # Sicherheitsrelevante Events


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
        LogLevel.LOADING: Fore.BLUE,
        LogLevel.PROCESSING: Fore.LIGHTCYAN_EX,
        LogLevel.PROGRESS: Fore.LIGHTBLUE_EX,
        LogLevel.WAITING: Fore.LIGHTYELLOW_EX,
        LogLevel.NOTICE: Fore.LIGHTMAGENTA_EX,
        LogLevel.WARN: Fore.YELLOW,
        LogLevel.ERROR: Fore.RED,
        LogLevel.CRITICAL: Fore.MAGENTA,
        LogLevel.FATAL: Fore.WHITE + Back.RED,
        LogLevel.SECURITY: Fore.BLACK + Back.YELLOW,
    }
    
    @classmethod
    def get_color(cls, level: LogLevel) -> str:
        """Gibt die Farbe für ein Log-Level zurück"""
        return cls.COLORS.get(level, Fore.WHITE)