"""
Logs Package - Professional Terminal Logger
PyNum Style Naming Convention

Zentrale Imports für einfache Verwendung.
Diese Datei geht davon aus, dass logger.py, category.py und loglevel.py
in einer einzigen logger.py zusammengeführt wurden.
"""

# Importiere alles aus der zusammengeführten logger.py
from .logger import (
    Logs,
    Category,
    CategoryColors,
    LogLevel,
    LogFormat,
    LevelColors
)

__all__ = [
    # Main Logger
    "Logs",
    "LogContext",
    
    # Categories
    "Category",
    "CategoryColors",
    
    # Levels & Formats
    "LogLevel",
    "LogFormat",
    "LevelColors",
    
    # Helper Functions
    "quick_start",
    "C",
]

class LogContext:
    """
    Context Manager für temporäre Log-Kontexte.
    
    Verwendung:
        with LogContext("USER_UPDATE"):
            Logs.info(Category.USER, "Updating user...")
    """
    def __init__(self, context: str):
        self.context = context

    def __enter__(self):
        Logs.push_context(self.context)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        Logs.pop_context()


# Quick-Start Konfiguration
def quick_start(
    log_file: str = "app.log",
    min_level: LogLevel = LogLevel.INFO,
    show_metadata: bool = False,
    colorize: bool = True,
    auto_flush: bool = True
) -> None:
    """
    Quick-Start Konfiguration für schnellen Einstieg.
    
    Args:
        log_file: Pfad zur Log-Datei
        min_level: Minimales Log-Level
        show_metadata: Zeige Datei/Zeile an
        colorize: Farbige Ausgabe
        auto_flush: Automatisches Flushen
    
    Example:
        >>> from logs import quick_start, Logs, Category
        >>> quick_start()
        >>> Logs.info(Category.SYSTEM, "App started")
    """
    # Basis-Konfiguration über configure
    Logs.configure(
        log_file=log_file,
        min_level=min_level,
        show_metadata=show_metadata
    )
    
    # Zusätzliche Attribute direkt setzen (da configure diese ggf. nicht alle als Arg nimmt)
    Logs.colorize = colorize
    Logs.auto_flush = auto_flush


# Convenience Imports für häufig genutzte Kategorien
class C:
    """
    Shorthand für häufig genutzte Kategorien.
    
    Verwendung:
        >>> from logs import Logs, C
        >>> Logs.info(C.SYS, "System started")  # statt Category.SYSTEM
    """
    # Core System
    API = Category.API
    DB = Category.DATABASE
    SYS = Category.SYSTEM
    AUTH = Category.AUTH
    CFG = Category.CONFIG
    
    # Network
    NET = Category.NETWORK
    HTTP = Category.HTTP
    WS = Category.WEBSOCKET
    
    # Security
    SEC = Category.SECURITY
    
    # Storage
    FILE = Category.FILE
    
    # Bot Specific (Discord)
    BOT = Category.BOT
    COGS = Category.COGS
    CMD = Category.COMMANDS
    EVENT = Category.EVENTS
    GUILD = Category.GUILD
    MSG = Category.MESSAGE
    VOICE = Category.VOICE
    
    # Monitoring
    PERF = Category.PERFORMANCE
    HEALTH = Category.HEALTH
    METRICS = Category.METRICS
    
    # Common
    DEBUG = Category.DEBUG
    TEST = Category.TEST
    DEV = Category.DEV