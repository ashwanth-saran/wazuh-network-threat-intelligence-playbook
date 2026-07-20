# 🔄 Workflow Explanation

This document explains how the Network Threat Intelligence Playbook processes a Wazuh alert from start to finish.

---

# Workflow Overview

When Wazuh detects a suspicious network event, the alert is automatically forwarded to n8n for enrichment.

The workflow performs multiple threat intelligence lookups before sending a detailed notification to Telegram.

```
Wazuh
   │
   ▼
Python Integration
   │
   ▼
n8n Webhook
   │
   ▼
Extract Alert
   │
   ▼
Public IP Check
   │
   ▼
VirusTotal Lookup
   │
   ▼
Parse VirusTotal
   │
   ▼
AbuseIPDB Lookup
   │
   ▼
Parse AbuseIPDB
   │
   ▼
GeoIP Lookup
   │
   ▼
Parse GeoIP
   │
   ▼
Telegram Alert
```

---

# Step 1 - Wazuh Detection

Wazuh continuously monitors the system for security events.

For this project, we generated SSH authentication failures to test the workflow.

Example alert:

- Failed SSH Login
- Invalid User
- Brute Force Attempt

---

# Step 2 - Python Integration

A custom Python integration sends the Wazuh alert to the n8n webhook.

Responsibilities:

- Read the Wazuh alert
- Convert it to JSON
- Send it to n8n

---

# Step 3 - Extract Alert

The workflow extracts useful information from the alert.

Example fields:

- Source IP
- Rule ID
- Severity
- Description
- Agent Name
- Timestamp

---

# Step 4 - Public IP Check

Not every IP address needs threat intelligence.

The workflow checks whether the IP address is:

- Private
- Public

Private IPs skip the threat intelligence lookups.

Public IPs continue to the enrichment phase.

---

# Step 5 - VirusTotal Lookup

The public IP is sent to the VirusTotal API.

Information collected includes:

- Reputation
- Malicious detections
- Suspicious detections
- Harmless detections
- Country
- Network owner

---

# Step 6 - AbuseIPDB Lookup

The same IP address is checked against AbuseIPDB.

Information collected:

- Abuse Confidence Score
- Total Reports
- ISP
- Usage Type
- Last Reported Date

---

# Step 7 - GeoIP Lookup

The workflow retrieves geographical information.

Information collected:

- Country
- Region
- City
- ISP
- ASN
- Timezone

---

# Step 8 - Telegram Notification

Finally, a formatted message is sent to Telegram.

The message contains:

- Alert information
- VirusTotal results
- AbuseIPDB results
- GeoIP information

This allows the analyst to quickly assess the threat without manually checking multiple websites.

---

# Workflow Benefits

This automation helps security analysts by:

- Reducing investigation time
- Providing instant threat intelligence
- Eliminating repetitive manual lookups
- Improving incident response efficiency

---

# Future Enhancements

The next version of this project will include:

- File Integrity Monitoring (FIM)
- Windows Authentication Monitoring
- Malware Hash Enrichment
- Risk Scoring
- Automated Response Actions
