![SimpleColoredLogs](img/SimpleColoredLogs.png)
# Professional Terminal Logger

Ein vollständiger, produktionsreifer Logger mit erweiterten Features für Python-Anwendungen und Discord Bots.

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- 🎨 **Farbige Terminal-Ausgabe** mit **148** vordefinierten Kategorien
- 📁 **File-Logging** mit automatischer Rotation und Kompression
- 🎯 **13 Log-Levels** von TRACE bis SECURITY mit Status-Tracking
- 🧵 **Thread-safe** mit Lock-Mechanismus
- 📊 **Multiple Output-Formate** (Simple, Standard, Detailed, JSON)
- 🔒 **Sensitive Data Redaction** (Passwörter, API-Keys, Tokens)
- 🌐 **Correlation IDs** für Request-Tracing über Microservices
- 📡 **Remote Forwarding** zu Syslog/Logstash
- ⚙️ **Umgebungsvariablen-Support** für einfache Konfiguration
- 🤖 **24 Discord-spezifische Kategorien** für Bot-Entwicklung
- 🔔 **Alert System** mit Handler-Registrierung
- 📝 **Session Recording** für Debugging
- 🎭 **Custom Format Strings** pro Log-Level
- 🎲 **Sampling & Rate Limiting** für Performance-Optimierung
- 🔄 **Adaptive Logging** mit automatischer Level-Anpassung

-----

## 📦 Installation

```bash
pip install SimpleColoredLogs
```

-----

## 🎯 Quick Start

### Basic Usage

```python
from logger import logger, LogLevel, Category, C, DC

# Konfiguration
logger.configure(
    log_file="app.log",
    min_level=LogLevel.INFO,
    show_metadata=False
)

# Einfache Logs
logger.trace(Category.SYSTEM, "Detailed debug info")
logger.debug(Category.SYSTEM, "Debug information")
logger.info(Category.SYSTEM, "Application started")
logger.success(Category.DATABASE, "Connection established", host="localhost")
logger.loading(Category.CONFIG, "Loading configuration files...")
logger.processing(Category.WORKER, "Processing batch job", items=1000)
logger.progress(Category.WORKER, "Processing files", current=45, total=100)
logger.waiting(Category.API, "Waiting for API response...")
logger.notice(Category.SYSTEM, "Configuration changed", key="timeout")
logger.warn(Category.CACHE, "Hit rate low", rate=0.65)
logger.error(Category.API, "Request failed", status=500)
logger.critical(Category.DATABASE, "Connection pool exhausted")
logger.fatal(Category.SYSTEM, "Application crash", reason="OutOfMemory")
logger.security(Category.AUTH, "Unauthorized access attempt", ip="1.2.3.4")

# Exception Logging
try:
    raise ValueError("Something went wrong!")
except Exception as e:
    logger.error(Category.SYSTEM, "Critical error", exception=e)
```

### Hierarchischer Kategorie-Zugriff

```python
from logger import logger, C, DC

# Über C.* Accessor (hierarchisch)
logger.info(C.CORE.API, "API request received")
logger.success(C.NET.HTTP, "HTTP connection established")
logger.warn(C.SEC.FRAUD, "Suspicious activity detected")
logger.error(C.DATA.ETL, "Data transformation failed")

# Über DC.* für Discord Bot (flach)
logger.info(DC.BOT, "Bot starting...")
logger.success(DC.GATEWAY, "Connected to Discord")
logger.loading(DC.COGS, "Loading cogs...")

# Direkte Category Enums
logger.info(Category.API, "Direct enum usage")

# String-basiert (auch möglich!)
logger.info("CUSTOM_CATEGORY", "Custom category log")
```

### Discord Bot Usage

```python
from logger import logger, DC

### Discord Bot Usage

```python
from logger import logger, DC

# Bot Startup
logger.info(DC.BOT, "🤖 Discord Bot Starting")
logger.loading(DC.INTENTS, "Configuring intents...")
logger.success(DC.GATEWAY, "Connected to Discord", latency="42ms")

# Cog Loading
logger.push_context("CogLoader")
logger.loading(DC.COGS, "Loading cogs...")
logger.success(DC.COGS, "Loaded cog", name="MusicCog", commands=12)
logger.warn(DC.COGS, "Warning", name="AdminCog", reason="Missing dependency")
logger.pop_context()

# Command Execution
logger.info(DC.SLASH, "Command invoked", command="/play", user="User#1234")
logger.processing(DC.VOICE, "Joining voice channel...")
logger.success(DC.VOICE, "Joined voice channel", channel="Music", members=5)

# Events
logger.info(DC.EVENT, "on_member_join", member="NewUser#5678")
logger.info(DC.MSG, "Message received", author="User#1234", channel="general")

# Moderation
logger.warn(DC.MOD, "User kicked", user="BadUser#9999", reason="Spam")
logger.security(DC.AM, "AutoMod triggered", rule="No spam", action="timeout")

# Rate Limiting
logger.warn(DC.RL, "Rate limit hit", endpoint="/messages", retry_after=2.5)

# Sharding
logger.info(DC.SHARDING, "Shard ready", shard_id=0, guilds=150, latency="42ms")
```

### Advanced Features

```python
# Kontext-Management
logger.push_context("UserRegistration")
logger.loading(C.USER.BASE, "Starting registration...")
logger.success(C.CORE.AUTH, "User authenticated")
logger.info(C.TP.EMAIL, "Verification email sent")
logger.pop_context()

# Custom Format Strings
logger.set_custom_format(
    LogLevel.ERROR, 
    "🚨 [{timestamp}] {level.name} in {category.value}: {message}"
)

# Session Recording (für Debugging)
logger.start_session_recording()
# ... dein Code ...
logs = logger.stop_session_recording()
# logs enthält alle Logs als List[Dict]

# Alert Handler registrieren
def email_alert(level, category, message):
    send_email(f"ALERT: {level} in {category}: {message}")

logger.register_alert_handler(LogLevel.FATAL, email_alert)
```

-----

## 📊 Log Levels

| Level | Wert | Beschreibung |
| :--- | :--- | :--- |
| **TRACE** | -1 | Sehr detaillierte Debug-Infos |
| **DEBUG** | 0 | Standard Debug-Informationen |
| **INFO** | 1 | Allgemeine Informationen |
| **SUCCESS** | 2 | Erfolgreiche Operationen |
| **LOADING** | 3 | Lädt gerade etwas |
| **PROCESSING** | 4 | Verarbeitet Daten |
| **PROGRESS** | 5 | Fortschritts-Updates |
| **WAITING** | 6 | Wartet auf Ressourcen |
| **NOTICE** | 7 | Wichtige Hinweise |
| **WARN** | 8 | Warnungen |
| **ERROR** | 9 | Standard-Fehler |
| **CRITICAL** | 10 | Kritische Fehler |
| **FATAL** | 11 | Fatale Fehler (Absturz) |
| **SECURITY** | 12 | Sicherheitsvorfälle |

-----

## 🎨 Verfügbare Kategorien (148)

### Core System & Runtime

`API`, `DATABASE`, `SERVER`, `CACHE`, `AUTH`, `SYSTEM`, `CONFIG`, `SCHEMA`, `INDEX`, `QUERY`, `VIEW`, `TRANSACTION_COMMIT`, `NOSQL`,
`RELATIONAL_DB`, `SESSION_STORAGE`, `RUNTIME`, `COMPILER`, `DEPENDENCY`, `CLI`

**Zugriff via:** `C.CORE.API`, `C.CORE.DB`, `C.CORE.CFG`, etc.

### Network & Communication

`NETWORK`, `HTTP`, `WEBSOCKET`, `GRPC`, `GRAPHQL`, `REST`, `SOAP`, `LOAD_BALANCER`, `REVERSE_PROXY`, `DNS`, `CDN`, `GEOLOCATION`

**Zugriff via:** `C.NET.HTTP`, `C.NET.WS`, `C.NET.GQL`, etc.

### Security, Compliance & Fraud

`SECURITY`, `ENCRYPTION`, `FIREWALL`, `AUDIT`, `COMPLIANCE`, `VULNERABILITY`, `GDPR`, `HIPAA`, `PCI_DSS`, `IDP`, `MFA`, `RATE_LIMITER`, `FRAUD`

**Zugriff via:** `C.SEC.BASE`, `C.SEC.FRAUD`, `C.SEC.MFA`, etc.

### Frontend, UI & Internationalisierung

`CLIENT`, `UI`, `UX`, `SPA`, `SSR`, `STATE`, `COMPONENT`, `I18N`

**Zugriff via:** `C.UI.BASE`, `C.UI.SPA`, `C.UI.I18N`, etc.

### Storage, Files & Assets

`FILE`, `STORAGE`, `BACKUP`, `SYNC`, `UPLOAD`, `DOWNLOAD`, `ASSET`

**Zugriff via:** `C.STORAGE.FILE`, `C.STORAGE.BKP`, `C.STORAGE.ASSET`, etc.

### Messaging & Events

`QUEUE`, `EVENT`, `PUBSUB`, `KAFKA`, `RABBITMQ`, `REDIS`

**Zugriff via:** `C.MSG.QUEUE`, `C.MSG.KAFKA`, `C.MSG.REDIS`, etc.

### External Services

`EMAIL`, `SMS`, `NOTIFICATION`, `PAYMENT`, `BILLING`, `STRIPE`, `PAYPAL`

**Zugriff via:** `C.TP.EMAIL`, `C.TP.PAYMENT`, `C.TP.STRIPE`, etc.

### Monitoring & Observability

`METRICS`, `PERFORMANCE`, `HEALTH`, `MONITORING`, `TRACING`, `PROFILING`

**Zugriff via:** `C.MONITOR.METRICS`, `C.MONITOR.PERF`, `C.MONITOR.HEALTH`, etc.

### Data Processing & Transformation

`ETL`, `PIPELINE`, `WORKER`, `CRON`, `SCHEDULER`, `BATCH`, `STREAM`, `MAPPING`, `TRANSFORM`, `REPORTING`

**Zugriff via:** `C.DATA.ETL`, `C.DATA.PIPE`, `C.DATA.TRANSFORM`, etc.

### Business Logic, Finance & Inventory

`BUSINESS`, `WORKFLOW`, `TRANSACTION`, `ORDER`, `INVOICE`, `SHIPPING`, `ACCOUNTING`, `INVENTORY`

**Zugriff via:** `C.BIZ.BASE`, `C.BIZ.ORDER`, `C.BIZ.ACC`, etc.

### User Management

`USER`, `SESSION`, `REGISTRATION`, `LOGIN`, `LOGOUT`, `PROFILE`

**Zugriff via:** `C.USER.BASE`, `C.USER.LOGIN`, `C.USER.PROFILE`, etc.

### AI & ML

`AI`, `ML`, `TRAINING`, `INFERENCE`, `MODEL`

**Zugriff via:** `C.AI.BASE`, `C.AI.ML`, `C.AI.TRAIN`, etc.

### DevOps & Infrastructure

`DEPLOY`, `CI_CD`, `DOCKER`, `KUBERNETES`, `TERRAFORM`, `ANSIBLE`, `SERVERLESS`, `CONTAINER`, `IAC`, `VPC`, `AUTOSCALING`, `PROVISION`, `DEPROVISION`

**Zugriff via:** `C.DEVOPS.DOCKER`, `C.DEVOPS.K8S`, `C.DEVOPS.PROVISION`, etc.

### Testing & Quality

`TEST`, `UNITTEST`, `INTEGRATION`, `E2E`, `LOAD_TEST`

**Zugriff via:** `C.TEST.BASE`, `C.TEST.UNIT`, `C.TEST.E2E`, etc.

### Third Party Integrations

`SLACK`, `DISCORD`, `TWILIO`, `AWS`, `GCP`, `AZURE`

**Zugriff via:** `C.TP.SLACK`, `C.TP.AWS`, `C.TP.AZURE`, etc.

### Discord Bot Specific

`BOT`, `COGS`, `COMMANDS`, `EVENTS`, `VOICE`, `GUILD`, `MEMBER`, `CHANNEL`, `MESSAGE`, `REACTION`, `MODERATION`, `PERMISSIONS`, `EMBED`, `SLASH_CMD`, `BUTTON`, `MODAL`, `SELECT_MENU`, `AUTOMOD`, `WEBHOOK`, `PRESENCE`, `INTENTS`, `SHARDING`, `GATEWAY`, `RATELIMIT`

**Zugriff via:** `DC.BOT`, `DC.COGS`, `DC.SLASH`, `DC.GATEWAY`, etc.

### Development

`DEBUG`, `DEV`, `STARTUP`, `SHUTDOWN`, `MIGRATION`, `UPDATE`, `VERSION`

**Zugriff via:** `C.DEV.DEBUG`, `C.DEV.START`, `C.DEV.SHUT`, etc.

-----

## 🔒 Security Features

### Sensitive Data Redaction

```python
# In configure() aktivieren
logger.configure(enable_redaction=True)

# Automatisch erkannte Patterns:
# - Kreditkarten, SSN, Passwörter, API Keys, Tokens, Bearer Tokens

# Wird automatisch angewendet auf alle Logs
logger.info(C.CORE.API, "User login", password="secret123")
# Output: User login password=[REDACTED]
```

### Remote Log Forwarding

```python
# Zu Syslog/Logstash forwarden
logger.configure(
    enable_remote=True,
    remote_host="logserver.company.com",
    remote_port=514
)
```

-----

## ⚙️ Konfiguration

### Standard-Konfiguration

```python
from logger import logger, LogFormat, LogLevel

logger.configure(
    min_level=LogLevel.DEBUG,
    log_file="app.log",
    format_type=LogFormat.STANDARD,  # SIMPLE, STANDARD, DETAILED, JSON
    show_metadata=False,
    show_thread_id=False,
    enable_buffer=False,
    enable_redaction=True,
    enable_remote=False,
    remote_host=None,
    remote_port=514,
    category_filter=None,  # None = alle Kategorien
    exclude_categories=None,  # Kategorien ausschließen
    sampling_rate=1.0,  # 1.0 = 100% der Logs
    apply_env_vars=True  # Umgebungsvariablen anwenden
)
```

### Umgebungsvariablen

Der Logger unterstützt Konfiguration via Umgebungsvariablen:

```bash
# Log-Level setzen
export LOG_MIN_LEVEL=INFO

# Log-Datei
export LOG_FILE=/var/log/myapp.log

# Format
export LOG_FORMAT=JSON  # SIMPLE, STANDARD, DETAILED, JSON

# Farben deaktivieren
export LOG_COLORIZE=false

# Metadata anzeigen
export LOG_SHOW_METADATA=true

# Sampling (0.0 - 1.0)
export LOG_SAMPLING_RATE=0.5

# Remote Forwarding
export LOG_REMOTE_HOST=logserver.example.com
export LOG_REMOTE_PORT=514
```

**Priorität:** Umgebungsvariablen überschreiben die in `configure()` gesetzten Werte (wenn `apply_env_vars=True`).

### Kategorie-Filtering

```python
from logger import logger, Category

# Nur bestimmte Kategorien loggen
logger.configure(
    category_filter=[Category.API, Category.DATABASE, Category.AUTH]
)

# Bestimmte Kategorien ausschließen
logger.configure(
    exclude_categories=[Category.DEBUG, Category.TRACE]
)
```

### Sampling & Rate Limiting

```python
# Nur 10% der Logs ausgeben (für High-Traffic Apps)
logger.configure(sampling_rate=0.1)

# Rate Limiting aktivieren (Max 500 Logs/Minute pro Kategorie)
# Hinweis: Dies wird über _rate_limit_enabled und _max_logs_per_minute gesteuert
# Aktuell nicht direkt über configure() verfügbar, siehe Code
```

### Adaptive Logging

```python
# Auto-Anpassung bei hoher Last
# Wechselt zu WARN bei >100 Logs/Minute
# Hinweis: Über _auto_adjust_level gesteuert, nicht direkt in configure()
```

-----

## 📝 Log-Formate

### SIMPLE

```
[INFO] [API] Request received
```

### STANDARD (Default)

```
[2024-01-15 14:30:45] [INFO      ] [API] Request received
```

### DETAILED

```
[2024-01-15 14:30:45] [INFO      ] [API] [main.py:123] Request received
```

### JSON

```json
{"timestamp": "2024-01-15T14:30:45", "level": "INFO", "category": "API", "message": "Request received", "file": "main.py", "line": 123}
```

-----

## 🎯 Best Practices

### 1. Strukturierte Logs mit Key-Value Pairs

```python
logger.info(C.CORE.API, "Request processed",
          method="POST",
          endpoint="/api/users",
          status=200,
          duration_ms=45.2)
```

### 2. Context für zusammenhängende Operationen

```python
logger.push_context("OrderProcessing")
logger.loading(C.BIZ.ORDER, "Processing order...")
logger.processing(C.TP.PAYMENT, "Processing payment...")
logger.success(C.BIZ.SHIP, "Shipment created")
logger.pop_context()
```

### 3. Exception Handling

```python
try:
    risky_operation()
except Exception as e:
    logger.error(C.CORE.API, "Operation failed", exception=e)
    # Traceback wird automatisch hinzugefügt
```

### 4. Custom Format Strings

```python
# Eigenes Format für ERROR-Level
logger.set_custom_format(
    LogLevel.ERROR,
    "🚨 {timestamp} | {level.name} | {category.value} | {message}"
)
```

### 5. Session Recording für Debugging

```python
# Debug-Session starten
logger.start_session_recording()

# ... problematischer Code ...
logger.debug(C.DEV.DEBUG, "Step 1")
logger.debug(C.DEV.DEBUG, "Step 2")

# Session beenden und analysieren
logs = logger.stop_session_recording()
with open("debug_session.json", "w") as f:
    json.dump(logs, f, indent=2)
```

### 6. Alert Handler für kritische Events

```python
def send_slack_alert(level, category, message):
    slack.send_message(f"🚨 {level}: {message}")

def send_email_alert(level, category, message):
    email.send(to="admin@company.com", subject=f"CRITICAL: {category}", body=message)

logger.register_alert_handler(LogLevel.FATAL, send_slack_alert)
logger.register_alert_handler(LogLevel.FATAL, send_email_alert)
logger.register_alert_handler(LogLevel.SECURITY, send_slack_alert)
```

-----

## 🏗️ Architektur-Übersicht

### Kategorie-Zugriff

```
Category (Enum)           # Basis-Enums: Category.API, Category.DATABASE
    ↓
Accessor-Klassen          # CORE, NET, SEC, UI, etc.
    ↓
C (Hierarchisch)          # C.CORE.API, C.NET.HTTP
DC (Discord Flat)         # DC.BOT, DC.GATEWAY
```

### String-basierte Kategorien

Der Logger akzeptiert auch String-Kategorien für maximale Flexibilität:

```python
logger.info("CUSTOM_INIT", "My custom category")
logger.warn("TEMP_CATEGORY", "Temporary log category")
```

Unbekannte Strings werden als `CustomCategory`-Objekte behandelt und erhalten Standard-Farben.

-----

## 🔧 API-Referenz

### Logging-Methoden

```python
logger.trace(category, message, **kwargs)
logger.debug(category, message, **kwargs)
logger.info(category, message, **kwargs)
logger.success(category, message, **kwargs)
logger.loading(category, message, **kwargs)
logger.processing(category, message, **kwargs)
logger.progress(category, message, **kwargs)
logger.waiting(category, message, **kwargs)
logger.notice(category, message, **kwargs)
logger.warn(category, message, **kwargs)
logger.error(category, message, exception=None, **kwargs)
logger.critical(category, message, exception=None, **kwargs)
logger.fatal(category, message, exception=None, **kwargs)
logger.security(category, message, **kwargs)
```

### Kontext-Management

```python
logger.push_context(context: str)          # Context hinzufügen
logger.pop_context() -> Optional[str]      # Context entfernen
```

### Konfiguration

```python
logger.configure(**options)                           # Hauptkonfiguration
logger.set_custom_format(level, format_string)        # Custom Format pro Level
logger.register_alert_handler(level, handler)         # Alert Handler
logger.start_session_recording()                      # Recording starten
logger.stop_session_recording() -> List[Dict]         # Recording stoppen
```

-----

## 📄 License

MIT License

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

-----

Made with ❤️ for Python developers and Discord bot creators