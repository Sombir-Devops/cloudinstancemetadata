import requests

response = requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document')
metadata = response.json()
print(metadata)