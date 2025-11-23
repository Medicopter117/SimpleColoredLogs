"""
Log Categories - Zentrale Kategorie-Definitionen
PyNum Style Naming Convention
"""

from enum import Enum
from typing import ClassVar
from colorama import Fore, Style, Back


class Category(str, Enum):
    """Standard-Kategorien für Logs mit PyNum Naming"""
    
    # === Core System ===
    API = "API"
    DATABASE = "DATABASE"
    SERVER = "SERVER"
    CACHE = "CACHE"
    AUTH = "AUTH"
    SYSTEM = "SYSTEM"
    CONFIG = "CONFIG"
    
    # === Network & Communication ===
    NETWORK = "NETWORK"
    HTTP = "HTTP"
    WEBSOCKET = "WEBSOCKET"
    GRPC = "GRPC"
    GRAPHQL = "GRAPHQL"
    REST = "REST"
    SOAP = "SOAP"
    
    # === Security & Compliance ===
    SECURITY = "SECURITY"
    ENCRYPTION = "ENCRYPTION"
    FIREWALL = "FIREWALL"
    AUDIT = "AUDIT"
    COMPLIANCE = "COMPLIANCE"
    VULNERABILITY = "VULNERABILITY"
    
    # === Storage & Files ===
    FILE = "FILE"
    STORAGE = "STORAGE"
    BACKUP = "BACKUP"
    SYNC = "SYNC"
    UPLOAD = "UPLOAD"
    DOWNLOAD = "DOWNLOAD"
    
    # === Messaging & Events ===
    QUEUE = "QUEUE"
    EVENT = "EVENT"
    PUBSUB = "PUBSUB"
    KAFKA = "KAFKA"
    RABBITMQ = "RABBITMQ"
    REDIS = "REDIS"
    
    # === External Services ===
    EMAIL = "EMAIL"
    SMS = "SMS"
    NOTIFICATION = "NOTIFICATION"
    PAYMENT = "PAYMENT"
    BILLING = "BILLING"
    STRIPE = "STRIPE"
    PAYPAL = "PAYPAL"
    
    # === Monitoring & Observability ===
    METRICS = "METRICS"
    PERFORMANCE = "PERFORMANCE"
    HEALTH = "HEALTH"
    MONITORING = "MONITORING"
    TRACING = "TRACING"
    PROFILING = "PROFILING"
    
    # === Data Processing ===
    ETL = "ETL"
    PIPELINE = "PIPELINE"
    WORKER = "WORKER"
    CRON = "CRON"
    SCHEDULER = "SCHEDULER"
    BATCH = "BATCH"
    STREAM = "STREAM"
    
    # === Business Logic ===
    BUSINESS = "BUSINESS"
    WORKFLOW = "WORKFLOW"
    TRANSACTION = "TRANSACTION"
    ORDER = "ORDER"
    INVOICE = "INVOICE"
    SHIPPING = "SHIPPING"
    
    # === User Management ===
    USER = "USER"
    SESSION = "SESSION"
    REGISTRATION = "REGISTRATION"
    LOGIN = "LOGIN"
    LOGOUT = "LOGOUT"
    PROFILE = "PROFILE"
    
    # === AI & ML ===
    AI = "AI"
    ML = "ML"
    TRAINING = "TRAINING"
    INFERENCE = "INFERENCE"
    MODEL = "MODEL"
    
    # === DevOps & Infrastructure ===
    DEPLOY = "DEPLOY"
    CI_CD = "CI/CD"
    DOCKER = "DOCKER"
    KUBERNETES = "K8S"
    TERRAFORM = "TERRAFORM"
    ANSIBLE = "ANSIBLE"
    
    # === Testing & Quality ===
    TEST = "TEST"
    UNITTEST = "UNITTEST"
    INTEGRATION = "INTEGRATION"
    E2E = "E2E"
    LOAD_TEST = "LOAD_TEST"
    
    # === Third Party Integrations ===
    SLACK = "SLACK"
    DISCORD = "DISCORD"
    TWILIO = "TWILIO"
    AWS = "AWS"
    GCP = "GCP"
    AZURE = "AZURE"
    
    # === Discord Bot Specific ===
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
    
    # === Development ===
    DEBUG = "DEBUG"
    DEV = "DEV"
    STARTUP = "STARTUP"
    SHUTDOWN = "SHUTDOWN"
    MIGRATION = "MIGRATION"


class CategoryColors:
    """Farb-Mappings für Kategorien"""
    
    COLORS: ClassVar[dict] = {
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
    
    @classmethod
    def get_color(cls, category: Category) -> str:
        """Gibt die Farbe für eine Kategorie zurück"""
        return cls.COLORS.get(category, Style.BRIGHT)