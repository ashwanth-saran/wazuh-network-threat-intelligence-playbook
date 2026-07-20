# 🏗️ Project Architecture

This document explains how the Network Threat Intelligence Playbook is designed and how data flows through the automation pipeline.

---

# Architecture Overview

The project follows a simple event-driven architecture.

```
                   ┌─────────────────────────┐
                   │     Wazuh Manager       │
                   │ Detects Security Alerts │
                   └────────────┬────────────┘
                                │
                                ▼
                ┌─────────────────────────┐
                │ Custom Python Integration│
                │ Sends Alert to n8n       │
                └────────────┬────────────┘
                             │
                             ▼
                 ┌─────────────────────────┐
                 │     n8n Webhook         │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │   Extract Alert Data    │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │ Public / Private IP     │
                 │        Check            │
                 └────────────┬────────────┘
                              │
                 Public IP Only
                              │
                              ▼
           ┌───────────────────────────────────┐
           │        Threat Intelligence         │
           ├───────────────────────────────────┤
           │ VirusTotal                        │
           │ AbuseIPDB                         │
           │ GeoIP                             │
           └───────────────────────────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │ Telegram Notification   │
                 └─────────────────────────┘
```

---

# Components

## Wazuh Manager

The Wazuh Manager monitors endpoints and detects security events such as:

- SSH brute-force attempts
- Authentication failures
- Network attacks

When an alert reaches the configured severity level, it triggers the custom integration.

---

## Custom Python Integration

The Python script acts as a bridge between Wazuh and n8n.

Responsibilities:

- Read the Wazuh alert
- Convert it into JSON
- Send it to the n8n webhook
- Log successful and failed requests

---

## n8n Workflow

The n8n workflow orchestrates the automation.

It performs:

- Alert extraction
- Public IP validation
- Threat intelligence enrichment
- Telegram notification

---

## Threat Intelligence Services

### VirusTotal

Provides:

- Reputation score
- Malicious detections
- Suspicious detections
- Network owner

---

### AbuseIPDB

Provides:

- Abuse confidence score
- Total reports
- ISP
- Usage type
- Last reported date

---

### GeoIP

Provides:

- Country
- Region
- City
- ASN
- Organization
- Timezone

---

## Telegram

Telegram serves as the notification platform.

Instead of manually checking multiple threat intelligence websites, analysts receive enriched alerts in real time.

---

# Why this Architecture?

This design keeps each component focused on a single responsibility.

Benefits include:

- Easy to understand
- Easy to troubleshoot
- Modular design
- Scalable for future playbooks
- Simple to extend with new integrations

---

# Future Architecture

This project is the first playbook in a larger SOAR platform.

Future versions will introduce an Alert Router that directs different types of Wazuh alerts to specialized playbooks.

```
                    Wazuh
                      │
                      ▼
                Alert Router
                      │
     ┌────────┬────────┬────────┬────────┐
     ▼        ▼        ▼        ▼
  Network    FIM    Windows   Malware
     │        │        │        │
     ▼        ▼        ▼        ▼
 Threat Intelligence & Enrichment
                      │
                      ▼
               Risk Scoring Engine
                      │
                      ▼
            Notification & Response
```

This modular architecture makes it easier to add new automation workflows without modifying the existing playbooks.
