# 🔄 n8n Workflow

This folder contains the exported n8n workflow used in this project.

The workflow automates the enrichment of Wazuh security alerts by querying multiple threat intelligence services and sending the results to Telegram.

---

# Purpose

Instead of manually investigating suspicious IP addresses, the workflow automatically:

- Receives alerts from Wazuh
- Extracts important alert information
- Checks whether the IP address is public
- Enriches the alert using threat intelligence sources
- Sends a formatted notification to Telegram

This reduces investigation time and helps analysts respond to threats more efficiently.

---

# Folder Structure

```
n8n/
├── network-threat-intelligence.json
└── README.md
```

---

# Importing the Workflow

1. Open your n8n instance.
2. Select **Import Workflow**.
3. Choose the `network-threat-intelligence.json` file.
4. Import the workflow.
5. Configure the required credentials.
6. Activate the workflow.

---

# Required Credentials

Before activating the workflow, configure the following credentials:

| Service | Required |
|----------|----------|
| VirusTotal API | ✅ |
| AbuseIPDB API | ✅ |
| Telegram Bot | ✅ |
| GeoIP API (if applicable) | ✅ |

Never commit API keys or bot tokens to your GitHub repository.

---

# Workflow Overview

```
Webhook
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
   │
   ▼
Respond to Webhook
```

---

# Workflow Nodes

## 1. Webhook

Receives security alerts forwarded from the custom Wazuh integration.

**Purpose:**

- Accept incoming HTTP POST requests
- Trigger the workflow automatically

---

## 2. Extract Alert

Extracts important fields from the Wazuh alert.

Examples include:

- Source IP
- Rule ID
- Alert level
- Description
- Agent name
- Timestamp

---

## 3. Public IP Check

Determines whether the detected IP address is public or private.

If the IP address is private, the workflow skips threat intelligence lookups and finishes the execution.

---

## 4. VirusTotal Lookup

Queries the VirusTotal API to gather reputation information.

Retrieved information includes:

- Malicious detections
- Suspicious detections
- Harmless detections
- Network owner
- Country

---

## 5. Parse VirusTotal

Extracts only the relevant information from the VirusTotal API response.

This simplifies the data before passing it to the next node.

---

## 6. AbuseIPDB Lookup

Checks whether the IP address has been reported for malicious activity.

Collected information includes:

- Abuse Confidence Score
- Total reports
- ISP
- Usage type
- Last reported date

---

## 7. Parse AbuseIPDB

Formats the AbuseIPDB response into a clean and consistent structure for use in the final alert.

---

## 8. GeoIP Lookup

Retrieves geographic and network information about the IP address.

Typical information includes:

- Country
- Region
- City
- ASN
- Organization
- Timezone

---

## 9. Parse GeoIP

Formats the location data before sending it to Telegram.

---

## 10. Telegram Alert

Builds a readable message containing:

- Alert information
- VirusTotal results
- AbuseIPDB results
- GeoIP details

The enriched alert is then delivered to the configured Telegram chat.

---

## 11. Respond to Webhook

Returns a successful response to complete the webhook execution.

This confirms that the alert has been processed successfully.

---

# Customization

You can extend this workflow by adding additional enrichment sources, such as:

- AlienVault OTX
- GreyNoise
- Shodan
- URLhaus
- MISP
- CIRCL CVE Search

You can also send notifications to platforms such as:

- Slack
- Microsoft Teams
- Discord
- Email

---

# Best Practices

- Test each node individually before activating the workflow.
- Use environment variables or n8n credentials to store secrets securely.
- Monitor workflow executions for failed requests.
- Keep API keys private and rotate them when necessary.
- Export the workflow after making changes to maintain version history.

---

# Summary

This workflow demonstrates how low-code automation can improve Security Operations by combining Wazuh with external threat intelligence services. It provides a reusable foundation that can be expanded into a complete SOAR platform over time.
