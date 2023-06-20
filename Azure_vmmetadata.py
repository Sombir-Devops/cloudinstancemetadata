import requests

metadata_url = 'http://169.254.169.254/metadata/instance?api-version=2021-03-01'
headers = {'Metadata': 'true'}
response = requests.get(metadata_url, headers=headers)
metadata = response.json()
print(metadata)