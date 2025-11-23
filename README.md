# Professional Terminal Logger

Ein vollständiger, produktionsreifer Logger mit erweiterten Features für Python-Anwendungen und Discord Bots.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

### Core Features
- 🎨 **Farbige Terminal-Ausgabe** mit 90+ vordefinierten Kategorien
- 📁 **File-Logging** mit automatischer Rotation und Kompression
- 🎯 **Level & Kategorie-Filtering** für präzise Kontrolle
- 🧵 **Thread-safe** mit Lock-Mechanismus
- 📊 **Multiple Output-Formate** (Simple, Standard, Detailed, JSON)

### Security & Compliance
- 🔒 **Sensitive Data Redaction** (Passwörter, API-Keys, Tokens, Kreditkarten)
- 🔍 **Custom Regex-Patterns** für Datenschutz
- 📝 **Audit-Trail Support** für Compliance

### Distributed Systems
- 🌐 **Correlation IDs** für Request-Tracing über Microservices
- 🔗 **Trace & Span IDs** für verteiltes Tracing
- 📡 **Remote Log Forwarding** (Syslog-kompatibel)

### Performance & Scale
- 🎲 **Sampling** - Log nur X% der Messages
- ⏱️ **Rate Limiting** - Max N Logs pro Minute
- 🧠 **Adaptive Logging** - Automatische Level-Anpassung bei hoher Last
- 📦 **Buffer-System** für Batch-Processing

### Monitoring & Analytics
- 🏥 **Health Checks** - Logger-Status überwachen
- 📊 **Prometheus Metrics Export** - Integration mit Monitoring-Tools
- 📈 **Live-Statistiken** - Echtzeit-Insights
- 🎬 **Session Recording** - Vollständige Log-Aufzeichnung

### Debug & Development
- 🔍 **Debug Tools** - tail(), grep() für Log-Analyse
- ⚡ **Performance Tracking** - Automatische Zeitmessung
- 🎭 **Context Manager** - Verschachtelte Logs mit Kontext
- 📋 **Tabellen & Progress Bars** - Strukturierte Ausgabe

### Discord Bot Support
- 🤖 **24 Discord-spezifische Kategorien** für Bot-Entwicklung
- 🎮 Vollständige Unterstützung für Cogs, Commands, Events, Voice, etc.

## 📦 Installation

```bash
pip install SimpleColoredLogs
```

## 🎯 Quick Start

### Basic Usage

```python
from logs import Logs, LogLevel, Category

# Konfiguration
Logs.configure(
    log_file="app.log",
    min_level=LogLevel.INFO,
    show_metadata=False
)

# Einfache Logs
Logs.info(Category.SYSTEM, "Application started")
Logs.success(Category.DATABASE, "Connection established", host="localhost", port=5432)
Logs.warn(Category.CACHE, "Hit rate low", rate=0.65)
Logs.error(Category.API, "Request failed", status=500, endpoint="/api/users")

# Exception Logging mit Traceback
try:
    raise ValueError("Something went wrong!")
except Exception as e:
    Logs.exception(Category.SYSTEM, "Critical error", e)
```

### Discord Bot Usage

```python
from logs import Logs, Category

# Bot Startup
Logs.banner("🤖 Discord Bot Starting", Category.BOT)
Logs.info(Category.INTENTS, "Configuring intents", guilds=True, members=True)
Logs.success(Category.GATEWAY, "Connected to Discord", latency="42ms")

# Cog Loading
with Logs.context("CogLoader"):
    Logs.success(Category.COGS, "Loaded cog", name="MusicCog", commands=12)
    Logs.warn(Category.COGS, "Warning", name="AdminCog", reason="Missing dependency")

# Command Execution
Logs.info(Category.SLASH_CMD, "Command invoked", command="/play", user="User#1234")
Logs.success(Category.VOICE, "Joined voice channel", channel="Music", members=5)

# Events
Logs.info(Category.EVENTS, "on_member_join", member="NewUser#5678")
Logs.info(Category.MESSAGE, "Message received", author="User#1234", channel="general")

# Moderation
Logs.warn(Category.MODERATION, "User kicked", user="BadUser#9999", reason="Spam")
Logs.error(Category.AUTOMOD, "AutoMod triggered", rule="No spam", action="timeout")

# Rate Limiting
Logs.warn(Category.RATELIMIT, "Rate limit hit", endpoint="/messages", retry_after=2.5)

# Sharding
Logs.info(Category.SHARDING, "Shard ready", shard_id=0, guilds=150, latency="42ms")
```

### Advanced Features

```python
# Performance Tracking
Logs.performance("database_query", Category.DATABASE)
# ... do work ...
duration = Logs.performance("database_query", Category.DATABASE)  # Returns duration in ms

# Context Manager
with Logs.context("UserRegistration"):
    Logs.info(Category.USER, "Registration started", email="user@example.com")
    Logs.success(Category.AUTH, "User authenticated")
    Logs.info(Category.EMAIL, "Verification email sent")

# Event Logging (für Analytics)
Logs.log_event("purchase_completed", Category.BUSINESS,
               order_id=12345, amount=99.99, currency="EUR")

# Distributed Tracing
Logs.set_correlation_id("req-abc-123-xyz")
Logs.set_trace_id("trace-456")
Logs.info(Category.API, "Processing request", endpoint="/api/users")
Logs.clear_tracing()

# Tabellen
Logs.table(Category.METRICS,
           ["Service", "Status", "Response Time"],
           [["API", "UP", "45ms"],
            ["Database", "UP", "12ms"],
            ["Cache", "DOWN", "N/A"]])

# Progress Bar
for i in range(1, 101):
    Logs.progress(Category.WORKER, i, 100, "Processing files")
```

## 🎨 Verfügbare Kategorien

### Core System
`API`, `DATABASE`, `SERVER`, `CACHE`, `AUTH`, `SYSTEM`, `CONFIG`

### Network & Communication
`NETWORK`, `HTTP`, `WEBSOCKET`, `GRPC`, `GRAPHQL`, `REST`, `SOAP`

### Security & Compliance
`SECURITY`, `ENCRYPTION`, `FIREWALL`, `AUDIT`, `COMPLIANCE`, `VULNERABILITY`

### Storage & Files
`FILE`, `STORAGE`, `BACKUP`, `SYNC`, `UPLOAD`, `DOWNLOAD`

### Messaging & Events
`QUEUE`, `EVENT`, `PUBSUB`, `KAFKA`, `RABBITMQ`, `REDIS`

### External Services
`EMAIL`, `SMS`, `NOTIFICATION`, `PAYMENT`, `BILLING`, `STRIPE`, `PAYPAL`

### Monitoring & Observability
`METRICS`, `PERFORMANCE`, `HEALTH`, `MONITORING`, `TRACING`, `PROFILING`

### Data Processing
`ETL`, `PIPELINE`, `WORKER`, `CRON`, `SCHEDULER`, `BATCH`, `STREAM`

### Business Logic
`BUSINESS`, `WORKFLOW`, `TRANSACTION`, `ORDER`, `INVOICE`, `SHIPPING`

### User Management
`USER`, `SESSION`, `REGISTRATION`, `LOGIN`, `LOGOUT`, `PROFILE`

### AI & ML
`AI`, `ML`, `TRAINING`, `INFERENCE`, `MODEL`

### DevOps & Infrastructure
`DEPLOY`, `CI_CD`, `DOCKER`, `KUBERNETES`, `TERRAFORM`, `ANSIBLE`

### Testing & Quality
`TEST`, `UNITTEST`, `INTEGRATION`, `E2E`, `LOAD_TEST`

### Third Party Integrations
`SLACK`, `DISCORD`, `TWILIO`, `AWS`, `GCP`, `AZURE`

### Discord Bot Specific
`BOT`, `COGS`, `COMMANDS`, `EVENTS`, `VOICE`, `GUILD`, `MEMBER`, `CHANNEL`, `MESSAGE`, `REACTION`, `MODERATION`, `PERMISSIONS`, `EMBED`, `SLASH_CMD`, `BUTTON`, `MODAL`, `SELECT_MENU`, `AUTOMOD`, `WEBHOOK`, `PRESENCE`, `INTENTS`, `SHARDING`, `GATEWAY`, `RATELIMIT`

### Development
`DEBUG`, `DEV`, `STARTUP`, `SHUTDOWN`, `MIGRATION`

## 🔒 Security Features

### Sensitive Data Redaction

```python
# Aktivieren
Logs.enable_redaction()

# Automatisch erkannte Patterns:
# - Kreditkarten (16 Digits)
# - SSN (XXX-XX-XXXX)
# - Passwörter (password=...)
# - API Keys (api_key=...)
# - Tokens (token=...)
# - Bearer Tokens

# Custom Pattern hinzufügen
Logs.add_redact_pattern(r'secret_code:\s*\S+')

# Deaktivieren
Logs.disable_redaction()
```

### Remote Log Forwarding

```python
# Zu Syslog/Logstash/etc. forwarden
Logs.enable_remote_forwarding("logserver.company.com", 514)

# Deaktivieren
Logs.disable_remote_forwarding()
```

## 📊 Monitoring & Health

### Health Checks

```python
# Health Status abrufen
health = Logs.health_check()
print(health)
# {
#     "status": "healthy",
#     "total_logs": 1523,
#     "error_count": 12,
#     "error_rate": 0.008,
#     "buffer_size": 0,
#     "file_size_mb": 2.5,
#     "remote_enabled": True,
#     "redaction_enabled": True,
#     ...
# }

# Schöne Ausgabe
Logs.print_health()
```

### Statistiken

```python
# Statistiken abrufen
stats = Logs.stats(detailed=True)

# Schöne Ausgabe
Logs.print_stats()
```

### Prometheus Metrics

```python
# Metrics exportieren
metrics = Logs.export_metrics_prometheus()
print(metrics)
# # HELP logs_total Total number of logs by level
# # TYPE logs_total counter
# logs_total{level="INFO"} 1234
# logs_total{level="ERROR"} 56
# ...
```

## ⚙️ Konfiguration

### Vollständige Konfiguration

```python
Logs.configure(
    enabled=True,
    show_timestamp=True,
    timestamp_format="%Y-%m-%d %H:%M:%S",
    min_level=LogLevel.DEBUG,
    log_file="app.log",
    colorize=True,
    format_type=LogFormat.STANDARD,  # SIMPLE, STANDARD, DETAILED, JSON
    show_metadata=False,              # Zeigt Datei:Zeile
    show_thread_id=False,
    auto_flush=True,
    max_file_size=10 * 1024 * 1024,  # 10MB
    backup_count=3,
    buffer_enabled=False,
    buffer_flush_interval=5.0,
    category_filter=None,             # Nur bestimmte Kategorien
    excluded_categories=[],           # Kategorien ausschließen
    sampling_rate=1.0,                # 0.0 - 1.0
    enable_redaction=True,
    enable_compression=True
)
```

### Rate Limiting

```python
# Max 500 Logs pro Minute
Logs.enable_rate_limiting(max_per_minute=500)

# Deaktivieren
Logs.disable_rate_limiting()
```

### Sampling

```python
# Nur 10% der Logs ausgeben
Logs.set_sampling_rate(0.1)

# Zurück auf 100%
Logs.set_sampling_rate(1.0)
```

### Adaptive Logging

```python
# Auto-Anpassung bei hoher Last
Logs.enable_adaptive_logging(noise_threshold=100)  # 100 logs/min

# Deaktivieren
Logs.disable_adaptive_logging()
```

## 🔍 Debug Tools

### Tail - Letzte N Logs anzeigen

```python
last_logs = Logs.tail(20)
for log in last_logs:
    print(log)
```

### Grep - Logs durchsuchen

```python
# Suche nach Pattern
errors = Logs.grep("error", case_sensitive=False, max_results=100)
for error in errors:
    print(error)

# Regex-Support
api_errors = Logs.grep(r"API.*ERROR", case_sensitive=False)
```

## 🎬 Session Recording

```python
# Session starten
Logs.start_session()

# ... Logs werden aufgezeichnet ...

# Session stoppen und speichern
logs = Logs.stop_session(save_to="session.json")
```

## 🔔 Alert System

```python
def email_alert(level, category, message):
    # Sende Email bei kritischen Fehlern
    send_email(f"ALERT: {level} in {category}: {message}")

# Alert-Handler registrieren
Logs.add_alert(LogLevel.FATAL, email_alert)
Logs.add_alert(LogLevel.ERROR, email_alert)

# Cooldown setzen (verhindert Spam)
Logs.set_alert_cooldown(300)  # 5 Minuten
```

## 🎨 Custom Farben

```python
from colorama import Fore, Style

# Kategorie-Farben anpassen
Logs.configure_category_colors({
    "CUSTOM_CATEGORY": Fore.LIGHTMAGENTA_EX + Style.BRIGHT,
    Category.API: Fore.GREEN  # Überschreiben
})
```

## 🔧 Custom Handler

```python
def custom_handler(level, category, message, metadata):
    # Sende zu externem System
    send_to_external_system({
        "level": level.name,
        "category": category,
        "message": message,
        "metadata": metadata
    })

# Handler hinzufügen
Logs.add_handler(custom_handler)

# Handler entfernen
Logs.remove_handler(custom_handler)

# Alle Handler entfernen
Logs.clear_handlers()
```

## 📝 Log-Formate

### SIMPLE
```
[INFO] [API] Request received
```

### STANDARD (Default)
```
[2024-01-15 14:30:45] [INFO] [API] Request received
```

### DETAILED
```
[2024-01-15 14:30:45] [INFO] [API] [main.py:123] Request received
```

### JSON
```json
{"timestamp": "2024-01-15T14:30:45", "level": "INFO", "category": "API", "message": "Request received"}
```

## 🎯 Best Practices

### 1. Strukturierte Logs mit Key-Value Pairs

```python
Logs.info(Category.API, "Request processed",
          method="POST",
          endpoint="/api/users",
          status=200,
          duration_ms=45.2,
          user_id=12345)
```

### 2. Context für zusammenhängende Operationen

```python
with Logs.context("OrderProcessing"):
    Logs.info(Category.ORDER, "Order received", order_id=123)
    Logs.info(Category.PAYMENT, "Payment processing")
    Logs.success(Category.SHIPPING, "Shipment created")
```

### 3. Performance Tracking

```python
@Logs.measure(Category.DATABASE)
def expensive_database_query():
    # ... query ...
    pass
```

### 4. Event-basiertes Logging

```python
# Für Analytics/Business Intelligence
Logs.log_event("user_signup", Category.USER,
               user_id=123,
               plan="premium",
               referrer="google")
```

### 5. Correlation IDs für Microservices

```python
# Am Anfang jedes Requests
Logs.set_correlation_id(request.headers.get('X-Correlation-ID'))

# Alle Logs in diesem Request haben jetzt die gleiche ID
Logs.info(Category.API, "Processing request")
```

## 📄 License

MIT License 

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📞 Support

For issues and questions, please open an issue on GitHub.

---

Made with ❤️ for Python developers and Discord bot creators