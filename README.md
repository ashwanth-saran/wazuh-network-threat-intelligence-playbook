# Wazuh Network Threat Intelligence Playbook

## 📌 Overview

This project demonstrates how to automate threat intelligence enrichment for Wazuh alerts using n8n.

When Wazuh detects a network-based security event (such as an SSH brute-force attempt), the alert is automatically forwarded to n8n, enriched using multiple threat intelligence services, and delivered to Telegram in real time.

This project was built as a practical SOC automation (SOAR) playbook to reduce manual investigation time for security analysts.

---

## ✨ Features

- Automated Wazuh alert processing
- Public vs Private IP detection
- VirusTotal IP reputation lookup
- AbuseIPDB reputation lookup
- GeoIP enrichment
- Telegram notifications
- Python-based Wazuh integration
- n8n workflow automation

---

## 🏗 Architecture

```text
Wazuh Manager
      │
      ▼
Python Integration
      │
      ▼
n8n Webhook
      │
      ▼
Public IP Check
      │
      ▼
VirusTotal
      │
      ▼
AbuseIPDB
      │
      ▼
GeoIP
      │
      ▼
Telegram
```

---

## 🛠 Technologies Used

- Wazuh
- n8n
- Python
- VirusTotal API
- AbuseIPDB API
- GeoIP API
- Telegram Bot API
- Ubuntu Linux

---

## 📁 Project Structure

```text
architecture/
docs/
integrations/
n8n/
screenshots/
```

---

## 🚀 Future Improvements

- File Integrity Monitoring playbook
- Windows Authentication playbook
- Malware analysis playbook
- Sysmon playbook
- Risk scoring engine
- Automated response actions

---

## 👨‍💻 Author

**Ashwanth Saran**

- LinkedIn: https://www.linkedin.com/in/ashwanthsaran08/
- Portfolio: https://ashufoilo.netlify.app/

---

## 📄 License

This project is licensed under the MIT License.
