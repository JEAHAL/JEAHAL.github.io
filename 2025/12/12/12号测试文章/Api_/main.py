import json
import requests
url="https://api.dify.ai/v1"
headers = { "Authorization": "Bearer app-HWHLLMoT7Zz4ein0WcR4lFs3",
"Content-Type": "application/json", }
content_input = "1+1等于几"
payload = {
"inputs": {

 "Content_input":content_input },

 "response_mode": "streaming",

 "user": "abc-123"
}
workflow_response = requests.post(url, data=json.dumps(payload), headers=headers)
workflow_response = workflow_response.json()
print(workflow_response['data']['outputs']['output'])