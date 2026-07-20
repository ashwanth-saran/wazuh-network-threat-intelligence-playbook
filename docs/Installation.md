# 🚀 Installation Guide

This guide will help you set up the complete Network Threat Intelligence Playbook.

---

# Prerequisites

Before starting, make sure you have the following:

- Ubuntu Server
- Wazuh Manager
- Python 3
- n8n
- Telegram Bot
- VirusTotal API Key
- AbuseIPDB API Key

---

# Step 1 - Install Wazuh

Install Wazuh Manager by following the official documentation:

https://documentation.wazuh.com/

After installation, verify that the manager is running.

---

# Step 2 - Install n8n

Install n8n using Docker or Node.js.

Official documentation:

https://docs.n8n.io/

After installation, ensure the n8n service is running.

---

# Step 3 - Create a Telegram Bot

1. Open Telegram
2. Search for **BotFather**
3. Run:

```
/newbot
```

4. Save the Bot Token.

5. Get your Chat ID.

---

# Step 4 - Obtain API Keys

Create free accounts and generate API keys:

## VirusTotal

https://www.virustotal.com/

## AbuseIPDB

https://www.abuseipdb.com/

Store the API keys securely.

---

# Step 5 - Configure Wazuh Integration

Copy the custom Python integration into:

```
/var/ossec/integrations/
```

Make it executable:

```bash
chmod +x custom-n8n.py
```

Restart the Wazuh Manager:

```bash
sudo systemctl restart wazuh-manager
```

---

# Step 6 - Import the n8n Workflow

Import the workflow JSON file located in:

```
n8n/
```

Configure:

- VirusTotal API Key
- AbuseIPDB API Key
- Telegram Bot Token
- Chat ID

---

# Step 7 - Test the Workflow

Generate an SSH failed login event.

Verify that:

- Wazuh detects the event.
- n8n executes the workflow.
- VirusTotal enrichment succeeds.
- AbuseIPDB enrichment succeeds.
- Telegram receives the alert.

---

# Troubleshooting

If the workflow does not execute:

- Verify the webhook URL.
- Ensure the Wazuh integration is executable.
- Check the n8n execution logs.
- Verify your API keys.
- Confirm the Telegram Bot Token and Chat ID.

---

# Next Steps

You now have a working automated Network Threat Intelligence Playbook.

Explore the repository for additional documentation and future enhancements.
