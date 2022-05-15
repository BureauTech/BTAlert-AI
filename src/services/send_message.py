import requests
messageBody = {
  "username": "BTALERT",
  "text": "Mensagem de erro",
  "url": "http://localhost",
  "icon_emoji": ":fire:",
  "attachments": [
    {
      "color": "#2eb886",
      
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": """<https://localhost|[Teste] Mensagem teste, alerta teste>
                \n*Alert* - `critical` 
                \n*Description*: nginx:8000 of job nginx-vts has been down for more than 1 minutes.
                \n*Details*:
                \n\t• alertname*: `InstanceDown`
                \n\t• instance*: `nginx:8000`
                \n\t• job*: `nginx-vts`
                \n\t• monitor*: `bureautech-monitor`
                \n\t• severity*: `critical`"""
			}
		}
	]

    }
  ]
}

url_api = ''
requests.post(url_api, headers={
               "Content-type": "application/json"}, json=messageBody)
