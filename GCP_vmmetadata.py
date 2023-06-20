import requests

metadata_url = 'http://metadata.google.internal/computeMetadata/v1/?recursive=true'
headers = {'Metadata-Flavor': 'Google'}
response = requests.get(metadata_url, headers=headers)
metadata = response.text
print(metadata)