# 🛠️ Troubleshooting Guide

During the development of this project, several issues were encountered. This guide documents the most common problems and their solutions to help others who may build a similar setup.

---

# Issue 1 - n8n Workflow Only Worked When Clicking "Execute Workflow"

## Problem

The workflow executed only when the **Execute Workflow** button was pressed.

Automatic alerts from Wazuh were not triggering the workflow.

## Cause

The Wazuh integration was sending alerts to the **test webhook** instead of the **production webhook**.

Incorrect:

```
http://127.0.0.1:5678/webhook-test/wazuh-alerts
```

Correct:

```
http://127.0.0.1:5678/webhook/wazuh-alerts
```

## Solution

Update the webhook URL inside the custom Python integration and restart the Wazuh Manager.

---

# Issue 2 - Wazuh Integration Did Not Execute

## Problem

The custom integration script never ran.

## Cause

The script did not have execute permissions.

## Solution

Run:

```bash
chmod +x /var/ossec/integrations/custom-n8n.py
```

Restart Wazuh:

```bash
sudo systemctl restart wazuh-manager
```

---

# Issue 3 - Telegram Notifications Were Not Received

## Problem

No Telegram messages were delivered.

## Possible Causes

- Invalid Bot Token
- Incorrect Chat ID
- Telegram node configuration error

## Solution

Verify:

- Bot Token
- Chat ID
- Telegram credentials inside n8n

---

# Issue 4 - VirusTotal Lookup Failed

## Problem

VirusTotal returned an error.

## Possible Causes

- Invalid API key
- API rate limit exceeded
- Incorrect request URL

## Solution

- Verify the API key.
- Check the request URL.
- Review the HTTP Request node output.

---

# Issue 5 - AbuseIPDB Lookup Failed

## Problem

No response was received from AbuseIPDB.

## Possible Causes

- Invalid API key
- Missing HTTP headers
- Incorrect IP parameter

## Solution

Ensure the following headers are configured:

- Key
- Accept: application/json

---

# Issue 6 - GeoIP Lookup Failed

## Problem

GeoIP information was missing.

## Cause

The original GeoIP provider used an HTTP-only endpoint, which may not work in all environments.

## Solution

Use an HTTPS-compatible GeoIP service or another supported provider.

---

# Issue 7 - Private IP Addresses

## Problem

Threat intelligence APIs returned no useful information.

## Cause

Private IP addresses cannot be checked using public reputation services.

Examples:

- 192.168.x.x
- 10.x.x.x
- 172.16.x.x – 172.31.x.x

## Solution

Use an IF node to skip enrichment for private IP addresses.

---

# Debugging Tips

Useful log locations:

## Wazuh Logs

```
/var/ossec/logs/ossec.log
```

## Integration Logs

```
/var/ossec/logs/integrations.log
```

## n8n Executions

Open:

Executions → Select the failed execution → Review each node.

---

# Best Practices

- Never expose API keys in screenshots.
- Store credentials securely.
- Test each node individually before connecting the workflow.
- Keep the workflow modular and easy to troubleshoot.
- Document any configuration changes for future reference.

---

# Final Thoughts

Troubleshooting is an essential part of building security automation. Every issue solved improves your understanding of Wazuh, n8n, and API integrations, making future projects easier to build and maintain.
