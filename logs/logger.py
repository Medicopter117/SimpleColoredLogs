"""
Logs - Professional Terminal Logger
Ein vollständiger, produktionsreifer Logger mit erweiterten Features
"""

from datetime import datetime
from typing import Optional, Callable, Dict, Any, List, Union
from pathlib import Path
import sys
import threading
import inspect
from enum import IntEnum
import traceback
import json
import os
import time
import atexit
from collections import defaultdict, deque

from colorama import Fore, Style, Back, init

# Colorama initialisieren
init(autoreset=True)


class LogLevel(IntEnum):
    """Log-Level Definitionen"""
    TRACE = -1
    DEBUG = 0
    INFO = 1
    SUCCESS = 2
    WARN = 3
    ERROR = 4
    FATAL = 5


class Category:
    """Standard-Kategorien für Logs"""
    # Core System
    API = "API"
    DATABASE = "DATABASE"
    SERVER = "SERVER"
    CACHE = "CACHE"
    AUTH = "AUTH"
    SYSTEM = "SYSTEM"
    CONFIG = "CONFIG"
    
    # Network & Communication
    NETWORK = "NETWORK"
    HTTP = "HTTP"
    WEBSOCKET = "WEBSOCKET"
    GRPC = "GRPC"
    GRAPHQL = "GRAPHQL"
    REST = "REST"
    SOAP = "SOAP"
    
    # Security & Compliance
    SECURITY = "SECURITY"
    ENCRYPTION = "ENCRYPTION"
    FIREWALL = "FIREWALL"
    AUDIT = "AUDIT"
    COMPLIANCE = "COMPLIANCE"
    VULNERABILITY = "VULNERABILITY"
    
    # Storage & Files
    FILE = "FILE"
    STORAGE = "STORAGE"
    BACKUP = "BACKUP"
    SYNC = "SYNC"
    UPLOAD = "UPLOAD"
    DOWNLOAD = "DOWNLOAD"
    
    # Messaging & Events
    QUEUE = "QUEUE"
    EVENT = "EVENT"
    PUBSUB = "PUBSUB"
    KAFKA = "KAFKA"
    RABBITMQ = "RABBITMQ"
    REDIS = "REDIS"
    
    # External Services
    EMAIL = "EMAIL"
    SMS = "SMS"
    NOTIFICATION = "NOTIFICATION"
    PAYMENT = "PAYMENT"
    BILLING = "BILLING"
    STRIPE = "STRIPE"
    PAYPAL = "PAYPAL"
    
    # Monitoring & Observability
    METRICS = "METRICS"
    PERFORMANCE = "PERFORMANCE"
    HEALTH = "HEALTH"
    MONITORING = "MONITORING"
    TRACING = "TRACING"
    PROFILING = "PROFILING"
    
    # Data Processing
    ETL = "ETL"
    PIPELINE = "PIPELINE"
    WORKER = "WORKER"
    CRON = "CRON"
    SCHEDULER = "SCHEDULER"
    BATCH = "BATCH"
    STREAM = "STREAM"
    
    # Business Logic
    BUSINESS = "BUSINESS"
    WORKFLOW = "WORKFLOW"
    TRANSACTION = "TRANSACTION"
    ORDER = "ORDER"
    INVOICE = "INVOICE"
    SHIPPING = "SHIPPING"
    
    # User Management
    USER = "USER"
    SESSION = "SESSION"
    REGISTRATION = "REGISTRATION"
    LOGIN = "LOGIN"
    LOGOUT = "LOGOUT"
    PROFILE = "PROFILE"
    
    # AI & ML
    AI = "AI"
    ML = "ML"
    TRAINING = "TRAINING"
    INFERENCE = "INFERENCE"
    MODEL = "MODEL"
    
    # DevOps & Infrastructure
    DEPLOY = "DEPLOY"
    CI_CD = "CI/CD"
    DOCKER = "DOCKER"
    KUBERNETES = "K8S"
    TERRAFORM = "TERRAFORM"
    ANSIBLE = "ANSIBLE"
    
    # Testing & Quality
    TEST = "TEST"
    UNITTEST = "UNITTEST"
    INTEGRATION = "INTEGRATION"
    E2E = "E2E"
    LOAD_TEST = "LOAD_TEST"
    
    # Third Party Integrations
    SLACK = "SLACK"
    DISCORD = "DISCORD"
    TWILIO = "TWILIO"
    AWS = "AWS"
    GCP = "GCP"
    AZURE = "AZURE"
    
    # Discord Bot Specific
    BOT = "BOT"
    COGS = "COGS"
    COMMANDS = "COMMANDS"
    EVENTS = "EVENTS"
    VOICE = "VOICE"
    GUILD = "GUILD"
    MEMBER = "MEMBER"
    CHANNEL = "CHANNEL"
    MESSAGE = "MESSAGE"
    REACTION = "REACTION"
    MODERATION = "MODERATION"
    PERMISSIONS = "PERMISSIONS"
    EMBED = "EMBED"
    SLASH_CMD = "SLASH_CMD"
    BUTTON = "BUTTON"
    MODAL = "MODAL"
    SELECT_MENU = "SELECT_MENU"
    AUTOMOD = "AUTOMOD"
    WEBHOOK = "WEBHOOK"
    PRESENCE = "PRESENCE"
    INTENTS = "INTENTS"
    SHARDING = "SHARDING"
    GATEWAY = "GATEWAY"
    RATELIMIT = "RATELIMIT"
    
    # Development
    DEBUG = "DEBUG"
    DEV = "DEV"
    STARTUP = "STARTUP"
    SHUTDOWN = "SHUTDOWN"
    MIGRATION = "MIGRATION"


class LogFormat(IntEnum):
    """Output-Format Optionen"""
    SIMPLE = 0      # [LEVEL] [CATEGORY] MSG
    STANDARD = 1    # [TIMESTAMP] [LEVEL] [CATEGORY] MSG
    DETAILED = 2    # [TIMESTAMP] [LEVEL] [CATEGORY] [file.py:123] MSG
    JSON = 3        # JSON-Format für Log-Aggregation


class Logs:
    """
    Professional Terminal Logger mit erweiterten Features
    
    Features:
    - 🎨 Farbige Terminal-Ausgabe mit 90+ Standard-Kategorien
    - 📁 File-Logging mit automatischer Rotation
    - 🎯 Level-Filtering & Kategorie-Filtering
    - 🔍 Metadaten (Dateiname, Zeile, Funktion)
    - 🧵 Thread-safe mit Lock
    - 📊 JSON-Export für Log-Aggregation
    - ⚡ Performance-Tracking & Profiling
    - 🎭 Context-Manager für verschachtelte Logs
    - 📝 Strukturierte Logs mit Key-Value Pairs
    - 📈 Live-Statistiken & Dashboards
    - 🔔 Alert-System für kritische Fehler
    - 🎬 Session-Recording
    - 🔄 Buffer-System für Batch-Logging
    - 🔒 Sensitive Data Redaction
    - 🌐 Distributed Tracing (Correlation/Trace/Span IDs)
    - 📡 Remote Log Forwarding (Syslog)
    - 🎲 Sampling & Rate Limiting
    - 🧠 Adaptive Logging (Auto-Level-Adjustment)
    - 🗜️ Log Compression
    - 🏥 Health Checks
    - 🔍 Debug Tools (tail, grep)
    - 📊 Prometheus Metrics Export
    """
    
    # === Konfiguration ===
    enabled: bool = True
    show_timestamp: bool = True
    min_level: LogLevel = LogLevel.DEBUG
    log_file: Optional[Path] = None
    colorize: bool = True
    format_type: LogFormat = LogFormat.STANDARD
    
    # Erweiterte Optionen
    show_metadata: bool = False
    show_thread_id: bool = False
    auto_flush: bool = True
    max_file_size: Optional[int] = 10 * 1024 * 1024  # 10MB
    backup_count: int = 3
    
    # Filter
    _category_filter: Optional[List[str]] = None  # Nur bestimmte Kategorien loggen
    _excluded_categories: List[str] = []  # Kategorien ausschließen
    
    # Format-Strings
    timestamp_format: str = "%Y-%m-%d %H:%M:%S"
    message_color: str = Fore.WHITE
    
    # Buffer-System
    _buffer_enabled: bool = False
    _buffer: deque = deque(maxlen=1000)
    _buffer_flush_interval: float = 5.0  # Sekunden
    _last_flush: float = time.time()
    
    # Session Recording
    _session_recording: bool = False
    _session_logs: List[Dict[str, Any]] = []
    _session_start: Optional[datetime] = None
    
    # Alert-System
    _alert_handlers: Dict[LogLevel, List[Callable]] = defaultdict(list)
    _alert_cooldown: Dict[str, float] = {}  # Verhindert Alert-Spam
    _alert_cooldown_seconds: float = 60.0
    
    # Sensitive Data Redaction
    _redact_enabled: bool = False
    _redact_patterns: List[str] = [
        r'\b\d{16}\b',  # Kreditkarten
        r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
        r'password["\s:=]+\S+',  # Passwörter
        r'api[_-]?key["\s:=]+\S+',  # API Keys
        r'secret["\s:=]+\S+',  # Secrets
        r'token["\s:=]+\S+',  # Tokens
        r'Bearer\s+\S+',  # Bearer Tokens
    ]
    
    # Correlation & Tracing
    _correlation_id: Optional[str] = None
    _trace_id: Optional[str] = None
    _span_id: Optional[str] = None
    
    # Remote Forwarding
    _remote_host: Optional[str] = None
    _remote_port: Optional[int] = None
    _remote_enabled: bool = False
    
    # Sampling & Rate Limiting
    _sampling_rate: float = 1.0  # 1.0 = 100%
    _rate_limits: Dict[str, tuple] = {}  # {key: (count, window_start)}
    _max_logs_per_minute: int = 1000
    _rate_limit_enabled: bool = False
    
    # Adaptive Logging
    _auto_adjust_level: bool = False
    _noise_threshold: int = 100  # Logs pro Minute
    _last_adjust_time: float = time.time()
    
    # Compression
    _compression_enabled: bool = False
    
    # Interne State
    _lock = threading.Lock()
    _handlers: List[Callable] = []
    _category_colors: Dict[str, str] = {
        # Core System
        Category.API: Fore.BLUE,
        Category.DATABASE: Fore.MAGENTA,
        Category.SERVER: Fore.CYAN,
        Category.CACHE: Fore.YELLOW,
        Category.AUTH: Fore.RED,
        Category.SYSTEM: Fore.WHITE,
        Category.CONFIG: Fore.LIGHTMAGENTA_EX,
        
        # Network & Communication
        Category.NETWORK: Fore.LIGHTBLUE_EX,
        Category.HTTP: Fore.BLUE + Style.BRIGHT,
        Category.WEBSOCKET: Fore.LIGHTBLUE_EX + Style.BRIGHT,
        Category.GRPC: Fore.CYAN + Style.BRIGHT,
        Category.GRAPHQL: Fore.MAGENTA + Style.BRIGHT,
        Category.REST: Fore.BLUE,
        Category.SOAP: Fore.LIGHTBLUE_EX,
        
        # Security & Compliance
        Category.SECURITY: Fore.LIGHTRED_EX,
        Category.ENCRYPTION: Fore.RED + Style.BRIGHT,
        Category.FIREWALL: Fore.RED,
        Category.AUDIT: Fore.LIGHTRED_EX,
        Category.COMPLIANCE: Fore.MAGENTA,
        Category.VULNERABILITY: Fore.RED + Back.WHITE,
        
        # Storage & Files
        Category.FILE: Fore.LIGHTGREEN_EX,
        Category.STORAGE: Fore.LIGHTGREEN_EX,
        Category.BACKUP: Fore.GREEN,
        Category.SYNC: Fore.CYAN,
        Category.UPLOAD: Fore.GREEN + Style.BRIGHT,
        Category.DOWNLOAD: Fore.LIGHTGREEN_EX,
        
        # Messaging & Events
        Category.QUEUE: Fore.LIGHTCYAN_EX,
        Category.EVENT: Fore.LIGHTYELLOW_EX,
        Category.PUBSUB: Fore.LIGHTMAGENTA_EX,
        Category.KAFKA: Fore.WHITE + Style.BRIGHT,
        Category.RABBITMQ: Fore.LIGHTYELLOW_EX,
        Category.REDIS: Fore.RED,
        
        # External Services
        Category.EMAIL: Fore.LIGHTMAGENTA_EX,
        Category.SMS: Fore.LIGHTCYAN_EX,
        Category.NOTIFICATION: Fore.YELLOW,
        Category.PAYMENT: Fore.GREEN + Style.BRIGHT,
        Category.BILLING: Fore.LIGHTGREEN_EX,
        Category.STRIPE: Fore.LIGHTBLUE_EX,
        Category.PAYPAL: Fore.BLUE,
        
        # Monitoring & Observability
        Category.METRICS: Fore.LIGHTYELLOW_EX,
        Category.PERFORMANCE: Fore.LIGHTYELLOW_EX,
        Category.HEALTH: Fore.GREEN,
        Category.MONITORING: Fore.CYAN,
        Category.TRACING: Fore.LIGHTCYAN_EX,
        Category.PROFILING: Fore.YELLOW,
        
        # Data Processing
        Category.ETL: Fore.MAGENTA,
        Category.PIPELINE: Fore.CYAN,
        Category.WORKER: Fore.LIGHTBLUE_EX,
        Category.CRON: Fore.YELLOW,
        Category.SCHEDULER: Fore.LIGHTYELLOW_EX,
        Category.BATCH: Fore.LIGHTMAGENTA_EX,
        Category.STREAM: Fore.LIGHTCYAN_EX,
        
        # Business Logic
        Category.BUSINESS: Fore.WHITE + Style.BRIGHT,
        Category.WORKFLOW: Fore.CYAN,
        Category.TRANSACTION: Fore.GREEN,
        Category.ORDER: Fore.LIGHTGREEN_EX,
        Category.INVOICE: Fore.LIGHTYELLOW_EX,
        Category.SHIPPING: Fore.LIGHTBLUE_EX,
        
        # User Management
        Category.USER: Fore.LIGHTMAGENTA_EX,
        Category.SESSION: Fore.CYAN,
        Category.REGISTRATION: Fore.GREEN,
        Category.LOGIN: Fore.BLUE,
        Category.LOGOUT: Fore.LIGHTBLUE_EX,
        Category.PROFILE: Fore.MAGENTA,
        
        # AI & ML
        Category.AI: Fore.MAGENTA + Style.BRIGHT,
        Category.ML: Fore.LIGHTMAGENTA_EX,
        Category.TRAINING: Fore.YELLOW,
        Category.INFERENCE: Fore.LIGHTYELLOW_EX,
        Category.MODEL: Fore.CYAN,
        
        # DevOps & Infrastructure
        Category.DEPLOY: Fore.GREEN + Style.BRIGHT,
        Category.CI_CD: Fore.LIGHTGREEN_EX,
        Category.DOCKER: Fore.BLUE,
        Category.KUBERNETES: Fore.LIGHTBLUE_EX,
        Category.TERRAFORM: Fore.MAGENTA,
        Category.ANSIBLE: Fore.RED,
        
        # Testing & Quality
        Category.TEST: Fore.YELLOW,
        Category.UNITTEST: Fore.LIGHTYELLOW_EX,
        Category.INTEGRATION: Fore.CYAN,
        Category.E2E: Fore.LIGHTCYAN_EX,
        Category.LOAD_TEST: Fore.LIGHTMAGENTA_EX,
        
        # Third Party Integrations
        Category.SLACK: Fore.MAGENTA,
        Category.DISCORD: Fore.LIGHTBLUE_EX,
        Category.TWILIO: Fore.RED,
        Category.AWS: Fore.YELLOW,
        Category.GCP: Fore.LIGHTBLUE_EX,
        Category.AZURE: Fore.CYAN,
        
        # Discord Bot Specific
        Category.BOT: Fore.LIGHTBLUE_EX + Style.BRIGHT,
        Category.COGS: Fore.MAGENTA + Style.BRIGHT,
        Category.COMMANDS: Fore.CYAN + Style.BRIGHT,
        Category.EVENTS: Fore.LIGHTYELLOW_EX + Style.BRIGHT,
        Category.VOICE: Fore.LIGHTGREEN_EX,
        Category.GUILD: Fore.LIGHTMAGENTA_EX,
        Category.MEMBER: Fore.LIGHTCYAN_EX,
        Category.CHANNEL: Fore.BLUE,
        Category.MESSAGE: Fore.WHITE,
        Category.REACTION: Fore.YELLOW,
        Category.MODERATION: Fore.RED + Style.BRIGHT,
        Category.PERMISSIONS: Fore.LIGHTRED_EX,
        Category.EMBED: Fore.LIGHTBLUE_EX,
        Category.SLASH_CMD: Fore.CYAN + Style.BRIGHT,
        Category.BUTTON: Fore.GREEN,
        Category.MODAL: Fore.LIGHTMAGENTA_EX,
        Category.SELECT_MENU: Fore.LIGHTYELLOW_EX,
        Category.AUTOMOD: Fore.RED + Back.WHITE,
        Category.WEBHOOK: Fore.LIGHTCYAN_EX,
        Category.PRESENCE: Fore.LIGHTYELLOW_EX,
        Category.INTENTS: Fore.MAGENTA,
        Category.SHARDING: Fore.LIGHTBLUE_EX + Style.BRIGHT,
        Category.GATEWAY: Fore.CYAN,
        Category.RATELIMIT: Fore.YELLOW + Style.BRIGHT,
        
        # Development
        Category.DEBUG: Fore.LIGHTBLACK_EX,
        Category.DEV: Fore.CYAN,
        Category.STARTUP: Fore.GREEN,
        Category.SHUTDOWN: Fore.RED,
        Category.MIGRATION: Fore.LIGHTYELLOW_EX,
    }
    _context_stack: List[str] = []
    _performance_markers: Dict[str, float] = {}
    _log_count: Dict[LogLevel, int] = {level: 0 for level in LogLevel}
    _category_count: Dict[str, int] = defaultdict(int)
    _error_count_by_category: Dict[str, int] = defaultdict(int)
    
    # Level-Farben
    _level_colors: Dict[LogLevel, str] = {
        LogLevel.TRACE: Fore.LIGHTBLACK_EX,
        LogLevel.DEBUG: Fore.CYAN,
        LogLevel.INFO: Fore.WHITE,
        LogLevel.SUCCESS: Fore.GREEN,
        LogLevel.WARN: Fore.YELLOW,
        LogLevel.ERROR: Fore.RED,
        LogLevel.FATAL: Fore.WHITE + Back.RED,
    }
    
    @classmethod
    def _redact_sensitive_data(cls, message: str) -> str:
        """Entfernt sensible Daten aus Log-Messages"""
        if not cls._redact_enabled:
            return message
        
        import re
        redacted = message
        for pattern in cls._redact_patterns:
            redacted = re.sub(pattern, '[REDACTED]', redacted, flags=re.IGNORECASE)
        return redacted
    
    @classmethod
    def _should_sample(cls) -> bool:
        """Prüft ob Log gesampelt werden soll"""
        if cls._sampling_rate >= 1.0:
            return True
        import random
        return random.random() < cls._sampling_rate
    
    @classmethod
    def _check_rate_limit(cls, category: str) -> bool:
        """Prüft Rate-Limit für Kategorie"""
        if not cls._rate_limit_enabled:
            return True
        
        current_time = time.time()
        key = f"rate_limit_{category}"
        
        if key in cls._rate_limits:
            count, window_start = cls._rate_limits[key]
            
            # Neues Fenster?
            if current_time - window_start > 60:
                cls._rate_limits[key] = (1, current_time)
                return True
            
            # Limit erreicht?
            if count >= cls._max_logs_per_minute:
                return False
            
            cls._rate_limits[key] = (count + 1, window_start)
            return True
        else:
            cls._rate_limits[key] = (1, current_time)
            return True
    
    @classmethod
    def _auto_adjust_log_level(cls):
        """Passt Log-Level automatisch an bei hoher Last"""
        if not cls._auto_adjust_level or not cls._session_start:
            return
        
        current_time = time.time()
        if current_time - cls._last_adjust_time < 60:
            return
        
        cls._last_adjust_time = current_time
        
        duration = (datetime.now() - cls._session_start).total_seconds() / 60
        if duration > 0:
            current_rate = sum(cls._log_count.values()) / duration
            
            if current_rate > cls._noise_threshold:
                if cls.min_level < LogLevel.WARN:
                    cls.min_level = LogLevel.WARN
                    cls.warn(Category.SYSTEM, f"Auto-adjusted log level to WARN (rate: {current_rate:.1f}/min)")
    
    @classmethod
    def _send_to_remote(cls, message: str):
        """Sendet Log zu Remote-Server (Syslog-Style)"""
        if not cls._remote_enabled or not cls._remote_host:
            return
        
        import socket
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            sock.sendto(message.encode('utf-8'), (cls._remote_host, cls._remote_port))
            sock.close()
        except Exception:
            pass  # Silent fail für Remote-Logging
    
    @classmethod
    def _compress_old_logs(cls):
        """Komprimiert alte Log-Dateien"""
        if not cls._compression_enabled or not cls.log_file:
            return
        
        import gzip
        try:
            for i in range(1, cls.backup_count + 1):
                old_file = cls.log_file.with_suffix(f"{cls.log_file.suffix}.{i}")
                gz_file = Path(f"{old_file}.gz")
                
                if old_file.exists() and not gz_file.exists():
                    with open(old_file, 'rb') as f_in:
                        with gzip.open(gz_file, 'wb') as f_out:
                            f_out.writelines(f_in)
                    old_file.unlink()
        except Exception as e:
            print(f"[Logs] Compression-Fehler: {e}", file=sys.stderr)
    
    @classmethod
    def _get_metadata(cls, frame_depth: int) -> Dict[str, Any]:
        """Holt Metadaten vom Aufrufer"""
        try:
            frame = inspect.stack()[frame_depth]
            metadata = {
                "file": Path(frame.filename).name,
                "line": frame.lineno,
                "function": frame.function,
                "thread": threading.current_thread().name if cls.show_thread_id else None
            }
            
            # Tracing-IDs hinzufügen
            if cls._correlation_id:
                metadata["correlation_id"] = cls._correlation_id
            if cls._trace_id:
                metadata["trace_id"] = cls._trace_id
            if cls._span_id:
                metadata["span_id"] = cls._span_id
            
            return metadata
        except Exception:
            return {"file": "", "line": 0, "function": "", "thread": None}
    
    @classmethod
    def _format_json(cls, level: LogLevel, category: str, message: str, metadata: Dict[str, Any], extra: Optional[Dict] = None) -> str:
        """Formatiert Log als JSON"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "level": level.name,
            "category": category,
            "message": message,
            **metadata
        }
        if cls._context_stack:
            log_entry["context"] = " > ".join(cls._context_stack)
        if extra:
            log_entry["extra"] = extra
        return json.dumps(log_entry, ensure_ascii=False)
    
    @classmethod
    def _format_colored(cls, level: LogLevel, category: str, message: str, metadata: Dict[str, Any], extra: Optional[Dict] = None) -> str:
        """Formatiert farbigen Log-Output"""
        level_name = level.name
        level_color = cls._level_colors.get(level, Fore.WHITE)
        category_color = cls._category_colors.get(category, Style.BRIGHT)
        
        # Timestamp
        timestamp_part = ""
        if cls.show_timestamp and cls.format_type != LogFormat.SIMPLE:
            ts = datetime.now().strftime(cls.timestamp_format)
            timestamp_part = f"{Style.DIM}[{ts}]{Style.RESET_ALL} "
        
        # Level - FETT und in Klammern
        padded_level = f"{level_name:<7}"
        level_part = f"{level_color}{Style.BRIGHT}[{padded_level}]{Style.RESET_ALL}"
        
        # Category mit optionaler Farbe
        category_part = f"{category_color}[{category}]{Style.RESET_ALL}"
        
        # Kontext
        context_part = ""
        if cls._context_stack:
            context = " > ".join(cls._context_stack)
            context_part = f"{Style.DIM}({context}){Style.RESET_ALL} "
        
        # Metadata (Datei:Zeile)
        metadata_part = ""
        if cls.show_metadata and cls.format_type == LogFormat.DETAILED:
            metadata_part = f"{Style.DIM}[{metadata['file']}:{metadata['line']}]{Style.RESET_ALL} "
        
        # Thread ID
        thread_part = ""
        if cls.show_thread_id and metadata.get('thread'):
            thread_part = f"{Style.DIM}[{metadata['thread']}]{Style.RESET_ALL} "
        
        # Tracing IDs
        tracing_part = ""
        if cls._correlation_id:
            tracing_part += f"{Style.DIM}[corr:{cls._correlation_id[:8]}]{Style.RESET_ALL} "
        
        # Extra Key-Value Pairs
        extra_part = ""
        if extra:
            extra_str = " ".join(f"{Style.DIM}{k}={v}{Style.RESET_ALL}" for k, v in extra.items())
            extra_part = f"{extra_str} "
        
        # Message
        msg_color = Fore.RED if level >= LogLevel.ERROR else cls.message_color
        message_part = f"{msg_color}{message}{Style.RESET_ALL}"
        
        return f"{timestamp_part}{level_part} {category_part} {thread_part}{tracing_part}{metadata_part}{context_part}{extra_part}{message_part}"
    
    @classmethod
    def _should_log_category(cls, category: str) -> bool:
        """Prüft ob Kategorie geloggt werden soll"""
        if category in cls._excluded_categories:
            return False
        if cls._category_filter and category not in cls._category_filter:
            return False
        return True
    
    @classmethod
    def _trigger_alerts(cls, level: LogLevel, category: str, message: str):
        """Triggert Alert-Handler für kritische Logs"""
        if level in cls._alert_handlers:
            alert_key = f"{level.name}:{category}"
            current_time = time.time()
            
            # Cooldown-Check
            if alert_key in cls._alert_cooldown:
                if current_time - cls._alert_cooldown[alert_key] < cls._alert_cooldown_seconds:
                    return  # Noch im Cooldown
            
            cls._alert_cooldown[alert_key] = current_time
            
            for handler in cls._alert_handlers[level]:
                try:
                    handler(level, category, message)
                except Exception as e:
                    print(f"[Logs] Alert-Handler-Fehler: {e}", file=sys.stderr)
    
    @classmethod
    def _rotate_log_file(cls):
        """Rotiert Log-Datei wenn zu groß"""
        if not cls.log_file or not cls.max_file_size:
            return
        
        try:
            if cls.log_file.exists() and cls.log_file.stat().st_size > cls.max_file_size:
                for i in range(cls.backup_count - 1, 0, -1):
                    old_file = cls.log_file.with_suffix(f"{cls.log_file.suffix}.{i}")
                    new_file = cls.log_file.with_suffix(f"{cls.log_file.suffix}.{i+1}")
                    if old_file.exists():
                        old_file.rename(new_file)
                
                cls.log_file.rename(cls.log_file.with_suffix(f"{cls.log_file.suffix}.1"))
        except Exception as e:
            print(f"[Logs] Rotation-Fehler: {e}", file=sys.stderr)
    
    @classmethod
    def _write_to_file(cls, message: str, is_json: bool = False):
        """Schreibt in Log-Datei mit Rotation"""
        if not cls.log_file:
            return
        
        cls._rotate_log_file()
        
        try:
            clean_message = message
            if not is_json:
                for code in list(Fore.__dict__.values()) + list(Style.__dict__.values()) + list(Back.__dict__.values()):
                    if isinstance(code, str):
                        clean_message = clean_message.replace(code, '')
            
            with open(cls.log_file, 'a', encoding='utf-8') as f:
                f.write(clean_message + '\n')
                if cls.auto_flush:
                    f.flush()
        except Exception as e:
            print(f"[Logs] File-Write-Fehler: {e}", file=sys.stderr)
    
    @classmethod
    def _flush_buffer(cls):
        """Flusht den Log-Buffer"""
        if not cls._buffer:
            return
        
        with cls._lock:
            while cls._buffer:
                log_entry = cls._buffer.popleft()
                cls._write_to_file(log_entry["output"], log_entry.get("is_json", False))
                print(log_entry["output"])
    
    @classmethod
    def _log(cls, level: LogLevel, category: str, message: str, extra: Optional[Dict] = None, frame_depth: int = 3):
        """Interne Log-Methode"""
        if not cls.enabled or level < cls.min_level:
            return
        
        if not cls._should_log_category(category):
            return
        
        # Sampling
        if not cls._should_sample():
            return
        
        # Rate Limiting
        if not cls._check_rate_limit(category):
            return
        
        # Adaptive Level Adjustment
        cls._auto_adjust_log_level()
        
        with cls._lock:
            cls._log_count[level] += 1
            cls._category_count[category] += 1
            
            if level >= LogLevel.ERROR:
                cls._error_count_by_category[category] += 1
            
            # Redact Sensitive Data
            message = cls._redact_sensitive_data(message)
            
            metadata = cls._get_metadata(frame_depth)
            
            # Format
            if cls.format_type == LogFormat.JSON:
                output = cls._format_json(level, category, message, metadata, extra)
                is_json = True
            else:
                output = cls._format_colored(level, category, message, metadata, extra)
                is_json = False
            
            # Session Recording
            if cls._session_recording:
                cls._session_logs.append({
                    "timestamp": datetime.now().isoformat(),
                    "level": level.name,
                    "category": category,
                    "message": message,
                    "metadata": metadata,
                    "extra": extra
                })
            
            # Buffer oder direkte Ausgabe
            if cls._buffer_enabled:
                cls._buffer.append({"output": output, "is_json": is_json})
                if time.time() - cls._last_flush > cls._buffer_flush_interval:
                    cls._flush_buffer()
                    cls._last_flush = time.time()
            else:
                # Console Output
                if level >= LogLevel.ERROR:
                    print(output, file=sys.stderr)
                else:
                    print(output)
                
                # File Output
                cls._write_to_file(output, is_json)
                
                # Remote Forwarding
                cls._send_to_remote(output)
            
            # Alerts
            cls._trigger_alerts(level, category, message)
            
            # Custom Handlers
            for handler in cls._handlers:
                try:
                    handler(level, category, message, metadata)
                except Exception as e:
                    print(f"[Logs] Handler-Fehler: {e}", file=sys.stderr)
    
    # === Public Logging Methods ===
    
    @classmethod
    def trace(cls, category: str, message: str, **kwargs):
        """TRACE Level - Sehr detaillierte Debug-Infos"""
        cls._log(LogLevel.TRACE, category, message, kwargs if kwargs else None)
    
    @classmethod
    def debug(cls, category: str, message: str, **kwargs):
        """DEBUG Level - Debug-Informationen"""
        cls._log(LogLevel.DEBUG, category, message, kwargs if kwargs else None)
    
    @classmethod
    def info(cls, category: str, message: str, **kwargs):
        """INFO Level - Allgemeine Informationen"""
        cls._log(LogLevel.INFO, category, message, kwargs if kwargs else None)
    
    @classmethod
    def success(cls, category: str, message: str, **kwargs):
        """SUCCESS Level - Erfolgreiche Operationen"""
        cls._log(LogLevel.SUCCESS, category, message, kwargs if kwargs else None)
    
    @classmethod
    def warn(cls, category: str, message: str, **kwargs):
        """WARN Level - Warnungen"""
        cls._log(LogLevel.WARN, category, message, kwargs if kwargs else None)
    
    @classmethod
    def error(cls, category: str, message: str, **kwargs):
        """ERROR Level - Fehler"""
        cls._log(LogLevel.ERROR, category, message, kwargs if kwargs else None)
    
    @classmethod
    def fatal(cls, category: str, message: str, **kwargs):
        """FATAL Level - Kritische Fehler"""
        cls._log(LogLevel.FATAL, category, message, kwargs if kwargs else None)
    
    @classmethod
    def exception(cls, category: str, message: str, exc: Optional[BaseException] = None):
        """ERROR mit Traceback"""
        full_message = f"{message}\n"
        if exc is not None:
            full_message += "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
        else:
            full_message += traceback.format_exc()
        cls._log(LogLevel.ERROR, category, full_message.strip(), frame_depth=3)
    
    # === Tracing & Correlation ===
    
    @classmethod
    def set_correlation_id(cls, correlation_id: str):
        """Setzt Correlation-ID für Request-Tracing"""
        cls._correlation_id = correlation_id
    
    @classmethod
    def set_trace_id(cls, trace_id: str):
        """Setzt Trace-ID"""
        cls._trace_id = trace_id
    
    @classmethod
    def set_span_id(cls, span_id: str):
        """Setzt Span-ID"""
        cls._span_id = span_id
    
    @classmethod
    def clear_tracing(cls):
        """Löscht alle Tracing-IDs"""
        cls._correlation_id = None
        cls._trace_id = None
        cls._span_id = None
    
    # === Remote Forwarding ===
    
    @classmethod
    def enable_remote_forwarding(cls, host: str, port: int = 514):
        """Aktiviert Remote Log-Forwarding (Syslog)"""
        cls._remote_host = host
        cls._remote_port = port
        cls._remote_enabled = True
        cls.info(Category.SYSTEM, f"Remote forwarding enabled: {host}:{port}")
    
    @classmethod
    def disable_remote_forwarding(cls):
        """Deaktiviert Remote Forwarding"""
        cls._remote_enabled = False
        cls.info(Category.SYSTEM, "Remote forwarding disabled")
    
    # === Sensitive Data Redaction ===
    
    @classmethod
    def enable_redaction(cls, custom_patterns: Optional[List[str]] = None):
        """Aktiviert Redaction von sensiblen Daten"""
        cls._redact_enabled = True
        if custom_patterns:
            cls._redact_patterns.extend(custom_patterns)
        cls.info(Category.SECURITY, "Sensitive data redaction enabled")
    
    @classmethod
    def disable_redaction(cls):
        """Deaktiviert Redaction"""
        cls._redact_enabled = False
    
    @classmethod
    def add_redact_pattern(cls, pattern: str):
        """Fügt Regex-Pattern für Redaction hinzu"""
        cls._redact_patterns.append(pattern)
    
    # === Sampling & Rate Limiting ===
    
    @classmethod
    def set_sampling_rate(cls, rate: float):
        """Setzt Sampling-Rate (0.0 - 1.0)"""
        cls._sampling_rate = max(0.0, min(1.0, rate))
        cls.info(Category.SYSTEM, f"Sampling rate set to {cls._sampling_rate * 100}%")
    
    @classmethod
    def enable_rate_limiting(cls, max_per_minute: int = 1000):
        """Aktiviert Rate-Limiting"""
        cls._rate_limit_enabled = True
        cls._max_logs_per_minute = max_per_minute
        cls.info(Category.SYSTEM, f"Rate limiting enabled: {max_per_minute}/min")
    
    @classmethod
    def disable_rate_limiting(cls):
        """Deaktiviert Rate-Limiting"""
        cls._rate_limit_enabled = False
    
    # === Adaptive Logging ===
    
    @classmethod
    def enable_adaptive_logging(cls, noise_threshold: int = 100):
        """Aktiviert automatische Log-Level-Anpassung"""
        cls._auto_adjust_level = True
        cls._noise_threshold = noise_threshold
        cls.info(Category.SYSTEM, f"Adaptive logging enabled (threshold: {noise_threshold}/min)")
    
    @classmethod
    def disable_adaptive_logging(cls):
        """Deaktiviert adaptive Logging"""
        cls._auto_adjust_level = False
    
    # === Compression ===
    
    @classmethod
    def enable_compression(cls):
        """Aktiviert Kompression alter Log-Dateien"""
        cls._compression_enabled = True
        cls._compress_old_logs()
        cls.info(Category.SYSTEM, "Log compression enabled")
    
    @classmethod
    def disable_compression(cls):
        """Deaktiviert Kompression"""
        cls._compression_enabled = False
    
    # === Health & Monitoring ===
    
    @classmethod
    def health_check(cls) -> Dict[str, Any]:
        """Gibt Health-Status des Loggers zurück"""
        total_logs = sum(cls._log_count.values())
        error_count = cls._log_count[LogLevel.ERROR] + cls._log_count[LogLevel.FATAL]
        
        file_size = 0
        if cls.log_file and cls.log_file.exists():
            file_size = cls.log_file.stat().st_size
        
        return {
            "status": "healthy" if error_count / max(total_logs, 1) < 0.1 else "degraded",
            "total_logs": total_logs,
            "error_count": error_count,
            "error_rate": error_count / max(total_logs, 1),
            "buffer_size": len(cls._buffer),
            "file_size_bytes": file_size,
            "file_size_mb": round(file_size / 1024 / 1024, 2),
            "enabled": cls.enabled,
            "min_level": cls.min_level.name,
            "remote_enabled": cls._remote_enabled,
            "redaction_enabled": cls._redact_enabled,
            "rate_limit_enabled": cls._rate_limit_enabled,
            "sampling_rate": cls._sampling_rate,
        }
    
    @classmethod
    def print_health(cls):
        """Druckt Health-Status"""
        health = cls.health_check()
        
        cls.separator("=", 60)
        cls.info(Category.HEALTH, f"🏥 Logger Health Check")
        cls.separator("=", 60)
        
        status_icon = "✅" if health["status"] == "healthy" else "⚠️"
        cls.info(Category.HEALTH, f"{status_icon} Status: {health['status'].upper()}")
        cls.info(Category.HEALTH, f"📊 Total Logs: {health['total_logs']}")
        cls.info(Category.HEALTH, f"❌ Errors: {health['error_count']} ({health['error_rate']*100:.1f}%)")
        cls.info(Category.HEALTH, f"💾 File Size: {health['file_size_mb']} MB")
        cls.info(Category.HEALTH, f"📦 Buffer: {health['buffer_size']} items")
        
        cls.separator("-", 60)
        cls.info(Category.HEALTH, "Features:")
        cls.info(Category.HEALTH, f"  Remote Forwarding: {'✅' if health['remote_enabled'] else '❌'}")
        cls.info(Category.HEALTH, f"  Redaction: {'✅' if health['redaction_enabled'] else '❌'}")
        cls.info(Category.HEALTH, f"  Rate Limiting: {'✅' if health['rate_limit_enabled'] else '❌'}")
        cls.info(Category.HEALTH, f"  Sampling: {health['sampling_rate']*100:.0f}%")
        
        cls.separator("=", 60)
    
    # === Debug Tools ===
    
    @classmethod
    def tail(cls, n: int = 10) -> List[str]:
        """Zeigt letzte N Logs aus Datei"""
        if not cls.log_file or not cls.log_file.exists():
            return []
        
        try:
            with open(cls.log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                return [line.strip() for line in lines[-n:]]
        except Exception as e:
            cls.error(Category.SYSTEM, f"Tail-Fehler: {e}")
            return []
    
    @classmethod
    def grep(cls, pattern: str, case_sensitive: bool = False, max_results: int = 100) -> List[str]:
        """Durchsucht Logs nach Pattern"""
        import re
        
        if not cls.log_file or not cls.log_file.exists():
            return []
        
        try:
            flags = 0 if case_sensitive else re.IGNORECASE
            results = []
            
            with open(cls.log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if re.search(pattern, line, flags):
                        results.append(line.strip())
                        if len(results) >= max_results:
                            break
            
            return results
        except Exception as e:
            cls.error(Category.SYSTEM, f"Grep-Fehler: {e}")
            return []
    
    @classmethod
    def export_metrics_prometheus(cls) -> str:
        """Exportiert Metrics im Prometheus-Format"""
        metrics = []
        
        metrics.append("# HELP logs_total Total number of logs by level")
        metrics.append("# TYPE logs_total counter")
        for level, count in cls._log_count.items():
            metrics.append(f'logs_total{{level="{level.name}"}} {count}')
        
        metrics.append("")
        metrics.append("# HELP logs_by_category Total number of logs by category")
        metrics.append("# TYPE logs_by_category counter")
        for category, count in cls._category_count.items():
            metrics.append(f'logs_by_category{{category="{category}"}} {count}')
        
        metrics.append("")
        metrics.append("# HELP logs_errors_by_category Error count by category")
        metrics.append("# TYPE logs_errors_by_category counter")
        for category, count in cls._error_count_by_category.items():
            metrics.append(f'logs_errors_by_category{{category="{category}"}} {count}')
        
        return "\n".join(metrics)
    
    @classmethod
    def log_event(cls, event_name: str, category: str, **attributes):
        """Strukturiertes Event-Logging für Analytics"""
        extra = {"event": event_name, **attributes}
        cls.info(category, f"Event: {event_name}", **extra)
    
    # === Advanced Features ===
    
    @classmethod
    def context(cls, context_name: str):
        """Context Manager für verschachtelte Logs"""
        return _LogContext(context_name)
    
    @classmethod
    def performance(cls, marker_name: str, category: str = Category.PERFORMANCE):
        """Performance Tracking"""
        if marker_name in cls._performance_markers:
            duration = (time.time() - cls._performance_markers[marker_name]) * 1000
            del cls._performance_markers[marker_name]
            cls.debug(category, f"{marker_name} completed", duration_ms=f"{duration:.2f}")
            return duration
        else:
            cls._performance_markers[marker_name] = time.time()
            return None
    
    @classmethod
    def measure(cls, category: str = Category.PERFORMANCE):
        """Decorator für Performance-Messung"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                marker = f"{func.__name__}"
                cls.performance(marker, category)
                try:
                    result = func(*args, **kwargs)
                    cls.performance(marker, category)
                    return result
                except Exception as e:
                    cls.performance(marker, category)
                    cls.exception(category, f"Error in {func.__name__}", e)
                    raise
            return wrapper
        return decorator
    
    @classmethod
    def table(cls, category: str, headers: List[str], rows: List[List[Any]]):
        """Logged eine Tabelle"""
        col_widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        
        header = " | ".join(h.ljust(w) for h, w in zip(headers, col_widths))
        separator = "-+-".join("-" * w for w in col_widths)
        
        cls.info(category, f"\n{header}\n{separator}")
        for row in rows:
            row_str = " | ".join(str(cell).ljust(w) for cell, w in zip(row, col_widths))
            cls.info(category, row_str)
    
    @classmethod
    def progress(cls, category: str, current: int, total: int, message: str = ""):
        """Progress Bar"""
        percentage = (current / total) * 100
        bar_length = 40
        filled = int(bar_length * current / total)
        bar = "█" * filled + "░" * (bar_length - filled)
        msg = f"{message} " if message else ""
        cls.info(category, f"{msg}[{bar}] {percentage:.1f}% ({current}/{total})")
    
    @classmethod
    def stats(cls, detailed: bool = False) -> Dict[str, Any]:
        """Gibt Log-Statistiken zurück"""
        stats_data = {
            "total": sum(cls._log_count.values()),
            "by_level": dict(cls._log_count),
            "by_category": dict(cls._category_count),
        }
        
        if detailed:
            stats_data["errors_by_category"] = dict(cls._error_count_by_category)
            stats_data["session_duration"] = None
            if cls._session_start:
                stats_data["session_duration"] = str(datetime.now() - cls._session_start)
        
        return stats_data
    
    @classmethod
    def print_stats(cls):
        """Druckt schöne Statistiken"""
        stats_data = cls.stats(detailed=True)
        
        cls.separator("=", 60)
        cls.info(Category.METRICS, f"📊 Log Statistics")
        cls.separator("=", 60)
        
        cls.info(Category.METRICS, f"Total Logs: {stats_data['total']}")
        
        cls.separator("-", 60)
        cls.info(Category.METRICS, "By Level:")
        for level, count in stats_data['by_level'].items():
            cls.info(Category.METRICS, f"  {level.name}: {count}")
        
        cls.separator("-", 60)
        cls.info(Category.METRICS, "Top Categories:")
        top_cats = sorted(stats_data['by_category'].items(), key=lambda x: x[1], reverse=True)[:5]
        for cat, count in top_cats:
            cls.info(Category.METRICS, f"  {cat}: {count}")
        
        cls.separator("=", 60)
    
    @classmethod
    def separator(cls, char: str = "=", length: int = 50):
        """Druckt eine Trennlinie"""
        print(f"{Style.DIM}{char * length}{Style.RESET_ALL}")
    
    @classmethod
    def banner(cls, text: str, category: str = Category.SYSTEM):
        """Druckt einen auffälligen Banner"""
        cls.separator("=", 60)
        cls.info(category, f"  {text}")
        cls.separator("=", 60)
    
    # === Session Recording ===
    
    @classmethod
    def start_session(cls):
        """Startet Session-Recording"""
        with cls._lock:
            cls._session_recording = True
            cls._session_start = datetime.now()
            cls._session_logs = []
            cls.info(Category.SYSTEM, "Session recording started")
    
    @classmethod
    def stop_session(cls, save_to: Optional[str] = None) -> List[Dict]:
        """Stoppt Session-Recording und gibt Logs zurück"""
        with cls._lock:
            cls._session_recording = False
            logs = cls._session_logs.copy()
            
            if save_to:
                with open(save_to, 'w', encoding='utf-8') as f:
                    json.dump(logs, f, indent=2, ensure_ascii=False)
                cls.success(Category.SYSTEM, f"Session saved to {save_to}")
            
            cls.info(Category.SYSTEM, f"Session stopped. Recorded {len(logs)} logs")
            return logs
    
    # === Alerts ===
    
    @classmethod
    def add_alert(cls, level: LogLevel, handler: Callable[[LogLevel, str, str], None]):
        """Fügt Alert-Handler für bestimmtes Level hinzu"""
        cls._alert_handlers[level].append(handler)
    
    @classmethod
    def set_alert_cooldown(cls, seconds: float):
        """Setzt Alert-Cooldown"""
        cls._alert_cooldown_seconds = seconds
    
    # === Configuration ===
    
    @classmethod
    def configure(cls,
                  enabled: Optional[bool] = None,
                  show_timestamp: Optional[bool] = None,
                  timestamp_format: Optional[str] = None,
                  min_level: Optional[LogLevel] = None,
                  log_file: Optional[str] = None,
                  colorize: Optional[bool] = None,
                  format_type: Optional[LogFormat] = None,
                  show_metadata: Optional[bool] = None,
                  show_thread_id: Optional[bool] = None,
                  auto_flush: Optional[bool] = None,
                  max_file_size: Optional[int] = None,
                  backup_count: Optional[int] = None,
                  buffer_enabled: Optional[bool] = None,
                  buffer_flush_interval: Optional[float] = None,
                  category_filter: Optional[List[str]] = None,
                  excluded_categories: Optional[List[str]] = None,
                  sampling_rate: Optional[float] = None,
                  enable_redaction: Optional[bool] = None,
                  enable_compression: Optional[bool] = None):
        """Konfiguriert den Logger"""
        with cls._lock:
            if enabled is not None:
                cls.enabled = enabled
            if show_timestamp is not None:
                cls.show_timestamp = show_timestamp
            if timestamp_format is not None:
                cls.timestamp_format = timestamp_format
            if min_level is not None:
                cls.min_level = min_level
            if log_file is not None:
                cls.log_file = Path(log_file) if log_file else None
            if colorize is not None:
                cls.colorize = colorize
            if format_type is not None:
                cls.format_type = format_type
            if show_metadata is not None:
                cls.show_metadata = show_metadata
            if show_thread_id is not None:
                cls.show_thread_id = show_thread_id
            if auto_flush is not None:
                cls.auto_flush = auto_flush
            if max_file_size is not None:
                cls.max_file_size = max_file_size
            if backup_count is not None:
                cls.backup_count = backup_count
            if buffer_enabled is not None:
                cls._buffer_enabled = buffer_enabled
            if buffer_flush_interval is not None:
                cls._buffer_flush_interval = buffer_flush_interval
            if category_filter is not None:
                cls._category_filter = category_filter
            if excluded_categories is not None:
                cls._excluded_categories = excluded_categories
            if sampling_rate is not None:
                cls.set_sampling_rate(sampling_rate)
            if enable_redaction is not None:
                if enable_redaction:
                    cls.enable_redaction()
                else:
                    cls.disable_redaction()
            if enable_compression is not None:
                if enable_compression:
                    cls.enable_compression()
                else:
                    cls.disable_compression()
    
    @classmethod
    def configure_category_colors(cls, color_map: Dict[str, str]):
        """Setzt Kategorie-Farben"""
        with cls._lock:
            cls._category_colors.update(color_map)
    
    @classmethod
    def add_handler(cls, handler: Callable[[LogLevel, str, str, Dict[str, Any]], None]):
        """Fügt Handler hinzu"""
        with cls._lock:
            cls._handlers.append(handler)
    
    @classmethod
    def remove_handler(cls, handler: Callable):
        """Entfernt Handler"""
        with cls._lock:
            if handler in cls._handlers:
                cls._handlers.remove(handler)
    
    @classmethod
    def clear_handlers(cls):
        """Entfernt alle Handler"""
        with cls._lock:
            cls._handlers.clear()
    
    @classmethod
    def reset(cls):
        """Reset auf Defaults"""
        with cls._lock:
            cls.enabled = True
            cls.show_timestamp = True
            cls.timestamp_format = "%Y-%m-%d %H:%M:%S"
            cls.min_level = LogLevel.DEBUG
            cls.log_file = None
            cls.colorize = True
            cls.format_type = LogFormat.STANDARD
            cls.show_metadata = False
            cls.show_thread_id = False
            cls.auto_flush = True
            cls.max_file_size = 10 * 1024 * 1024
            cls.backup_count = 3
            cls.message_color = Fore.WHITE
            cls._category_filter = None
            cls._excluded_categories = []
            cls._context_stack = []
            cls._performance_markers = {}
            cls._log_count = {level: 0 for level in LogLevel}
            cls._category_count = defaultdict(int)
            cls._error_count_by_category = defaultdict(int)
            cls._buffer_enabled = False
            cls._buffer.clear()
            cls._session_recording = False
            cls._session_logs = []
            cls._alert_handlers = defaultdict(list)
            cls._alert_cooldown = {}
            cls._correlation_id = None
            cls._trace_id = None
            cls._span_id = None
            cls._remote_enabled = False
            cls._redact_enabled = False
            cls._sampling_rate = 1.0
            cls._rate_limit_enabled = False
            cls._auto_adjust_level = False
            cls._compression_enabled = False
            cls.clear_handlers()


class _LogContext:
    """Context Manager für verschachtelte Logs"""
    def __init__(self, name: str):
        self.name = name
    
    def __enter__(self):
        Logs._context_stack.append(self.name)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if Logs._context_stack:
            Logs._context_stack.pop()


# Auto-Flush beim Beenden
@atexit.register
def _cleanup():
    """Cleanup beim Beenden"""
    if Logs._buffer_enabled:
        Logs._flush_buffer()
    if Logs._session_recording:
        Logs.stop_session()


# ============================================================================
# USAGE EXAMPLES (Optional - can be removed)
# ============================================================================
"""
Quick Start Examples:

# Basic Usage
from logs import Logs, Category, LogLevel

Logs.configure(log_file="app.log", min_level=LogLevel.INFO)
Logs.info(Category.SYSTEM, "Application started")
Logs.success(Category.DATABASE, "Connected", host="localhost")
Logs.error(Category.API, "Request failed", status=500)

# Discord Bot Usage
Logs.banner("🤖 Bot Starting", Category.BOT)
Logs.success(Category.GATEWAY, "Connected", latency="42ms")

with Logs.context("CogLoader"):
    Logs.success(Category.COGS, "Loaded cog", name="MusicCog")

Logs.info(Category.SLASH_CMD, "/play invoked", user="User#1234")
Logs.warn(Category.RATELIMIT, "Rate limit hit", retry_after=2.5)

# Advanced Features
Logs.enable_redaction()  # Hide sensitive data
Logs.set_correlation_id("req-123")  # Distributed tracing
Logs.enable_remote_forwarding("logserver.local", 514)

# Monitoring
Logs.print_health()
Logs.print_stats()
"""