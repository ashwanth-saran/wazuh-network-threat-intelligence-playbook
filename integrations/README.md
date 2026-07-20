# 🔗 Wazuh Integration

This folder contains the custom Python integration used to forward Wazuh alerts to the n8n workflow.

The integration acts as a bridge between Wazuh and the automation platform, allowing security alerts to be processed automatically.

---

# Purpose

By default, Wazuh can execute custom integration scripts whenever an alert matches specific rules or severity levels.

In this project, the custom integration performs the following tasks:

- Reads the Wazuh alert
- Converts the alert into JSON format
- Sends the alert to the n8n webhook
- Logs the request status for troubleshooting

---

# Integration Workflow

```
Wazuh Alert
      │
      ▼
custom-n8n.py
      │
      ▼
Convert Alert to JSON
      │
      ▼
HTTP POST Request
      │
      ▼
n8n Webhook
```

---

# File Structure

```
integrations/
├── custom-n8n.py
└── README.md
```

---

# Installation

Copy the integration script to the Wazuh integrations directory.

```
/var/ossec/integrations/
```

Grant execute permissions:

```bash
chmod +x /var/ossec/integrations/custom-n8n.py
```

Restart the Wazuh Manager:

```bash
sudo systemctl restart wazuh-manager
```

---

# Wazuh Configuration

Add the following integration block to the Wazuh configuration file (`ossec.conf`):

```xml
<integration>
  <name>custom-n8n</name>
  <hook_url>http://127.0.0.1:5678/webhook/wazuh-alerts</hook_url>
  <level>3</level>
  <alert_format>json</alert_format>
</integration>
```

After updating the configuration, restart the Wazuh Manager.

---

# Logging

The integration records its activity in:

```
/var/ossec/logs/integrations.log
```

This log can be used to verify successful requests and troubleshoot errors.

---

# Error Handling

The script includes basic exception handling to:

- Capture unexpected errors
- Prevent the integration from crashing
- Record failures in the integration log

---

# Customization

You can extend the script to support additional features, such as:

- Sending alerts to multiple webhooks
- Integrating with Slack or Microsoft Teams
- Adding authentication headers
- Filtering alerts before sending
- Triggering different workflows based on alert type

---

# Security Considerations

When deploying this integration:

- Protect API keys and webhook URLs.
- Restrict access to the Wazuh server.
- Monitor integration logs for unexpected activity.
- Keep the Python script updated with any workflow changes.

---

# Summary

The custom integration is a lightweight but important component of this project. It enables Wazuh to communicate with n8n, allowing security alerts to be enriched with threat intelligence and delivered to analysts automatically.
