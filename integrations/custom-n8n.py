#!/var/ossec/framework/python/bin/python3

import sys
import json
import requests
import logging

logging.basicConfig(
    filename="/var/ossec/logs/integrations.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

try:
    alert_file = sys.argv[1]
    api_key = sys.argv[2] if len(sys.argv) > 2 else ""
    hook_url = "http://127.0.0.1:5678/webhook/wazuh-alerts"
    with open(alert_file, "r") as f:
        alert = json.load(f)

    response = requests.post(
        hook_url,
        json=alert,
        timeout=15
    )

    logging.info(f"HTTP {response.status_code}")

except Exception as e:
    logging.exception(e)
