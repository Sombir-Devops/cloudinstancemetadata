# Fetching cloud instance metadata with python

## Problem Statement
We need to write code that will query the meta data of an instance within AWS or Azure or GCP and provide a json formatted output. The choice of language and implementation is up to you

## Solution
I have used the Instance Metadata Service(IMDS) from cloud providers
Make sure to run the code within an instance in the respective cloud provider to access the instance metadata. The code sends an HTTP request to the metadata endpoint and retrieves the metadata information. The json() method is used to parse the response and convert it to a Python dictionary for AWS and Azure, while for GCP, the metadata is returned as a string

### Here is the execution output for Azure VM metadata for feching combined as well as particular data key to be retrieved individually

=========================
som@myvm:~$ cat meta.py 
import requests

metadata_url = 'http://169.254.169.254/metadata/instance?api-version=2021-03-01'
headers = {'Metadata': 'true'}
response = requests.get(metadata_url, headers=headers)
metadata = response.json()
print(metadata)
som@myvm:~$ pwd
/home/som
som@myvm:~$ exit
logout
Connection to 168.62.21.119 closed.
============================
The jq utility is available in many cases, but not all. If the jq utility is missing, use | python -m json.tool instead.
curl -s -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | jq

curl -s -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute?api-version=2021-02-01" | jq

curl -s -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute?api-version=2021-01-01&format=json"


som@myvm:~$ sudo snap install jq
jq 1.5+dfsg-1 from Michael Vogt (mvo✪) installed
som@myvm:~$ curl -s -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | jq
{
  "compute": {
    "azEnvironment": "AzurePublicCloud",
    "customData": "",
    "evictionPolicy": "",
    "isHostCompatibilityLayerVm": "false",
    "licenseType": "",
    "location": "westus",
    "name": "myvm",
    "offer": "0001-com-ubuntu-server-focal",
    "osProfile": {
      "adminUsername": "som",
      "computerName": "myvm",
      "disablePasswordAuthentication": "false"
    },
    "osType": "Linux",
    "placementGroupId": "",
    "plan": {
      "name": "",
      "product": "",
      "publisher": ""
    },
    "platformFaultDomain": "0",
    "platformUpdateDomain": "0",
    "priority": "",
    "provider": "Microsoft.Compute",
    "publicKeys": [],
    "publisher": "canonical",
    "resourceGroupName": "MyResourceGroup",
    "resourceId": "/subscriptions/35b0fa4f-b6ba-4752-87a9-d644b3f23b8b/resourceGroups/MyResourceGroup/providers/Microsoft.Compute/virtualMachines/myvm",
    "securityProfile": {
      "secureBootEnabled": "false",
      "virtualTpmEnabled": "false"
    },
    "sku": "20_04-lts-gen2",
    "storageProfile": {
      "dataDisks": [],
      "imageReference": {
        "id": "",
        "offer": "0001-com-ubuntu-server-focal",
        "publisher": "canonical",
        "sku": "20_04-lts-gen2",
        "version": "latest"
      },
      "osDisk": {
        "caching": "ReadWrite",
        "createOption": "FromImage",
        "diffDiskSettings": {
          "option": ""
        },
        "diskSizeGB": "30",
        "encryptionSettings": {
          "enabled": "false"
        },
        "image": {
          "uri": ""
        },
        "managedDisk": {
          "id": "/subscriptions/35b0fa4f-b6ba-4752-87a9-d644b3f23b8b/resourceGroups/MyResourceGroup/providers/Microsoft.Compute/disks/myvm_disk1_14c1467024f349298ac0b1ecff9036be",
          "storageAccountType": "Premium_LRS"
        },
        "name": "myvm_disk1_14c1467024f349298ac0b1ecff9036be",
        "osType": "Linux",
        "vhd": {
          "uri": ""
        },
        "writeAcceleratorEnabled": "false"
      },
      "resourceDisk": {
        "size": "16384"
      }
    },
    "subscriptionId": "35b0fa4f-b6ba-4752-87a9-d644b3f23b8b",
    "tags": "",
    "tagsList": [],
    "userData": "",
    "version": "20.04.202305150",
    "vmId": "56cdefb2-0300-48a9-a9b6-883f2c828297",
    "vmScaleSetName": "",
    "vmSize": "Standard_D2s_v3",
    "zone": ""
  },
  "network": {
    "interface": [
      {
        "ipv4": {
          "ipAddress": [
            {
              "privateIpAddress": "10.0.0.4",
              "publicIpAddress": ""
            }
          ],
          "subnet": [
            {
              "address": "10.0.0.0",
              "prefix": "24"
            }
          ]
        },
        "ipv6": {
          "ipAddress": []
        },
        "macAddress": "000D3A3AEE3D"
      }
    ]
  }
}

som@myvm:~$ curl -s -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute?api-versio
n=2021-02-01" | jq
{
  "azEnvironment": "AzurePublicCloud",
  "customData": "",
  "evictionPolicy": "",
  "isHostCompatibilityLayerVm": "false",
  "licenseType": "",
  "location": "westus",
  "name": "myvm",
  "offer": "0001-com-ubuntu-server-focal",
  "osProfile": {
    "adminUsername": "som",
    "computerName": "myvm",
    "disablePasswordAuthentication": "false"
  },
  "osType": "Linux",
  "placementGroupId": "",
  "plan": {
    "name": "",
    "product": "",
    "publisher": ""
  },
  "platformFaultDomain": "0",
  "platformUpdateDomain": "0",
  "priority": "",
  "provider": "Microsoft.Compute",
  "publicKeys": [],
  "publisher": "canonical",
  "resourceGroupName": "MyResourceGroup",
  "resourceId": "/subscriptions/35b0fa4f-b6ba-4752-87a9-d644b3f23b8b/resourceGroups/MyResourceGroup/providers/Microsoft.Compute/virtualMachines/myvm",
  "securityProfile": {
    "secureBootEnabled": "false",
    "virtualTpmEnabled": "false"
  },
  "sku": "20_04-lts-gen2",
  "storageProfile": {
    "dataDisks": [],
    "imageReference": {
      "id": "",
      "offer": "0001-com-ubuntu-server-focal",
      "publisher": "canonical",
      "sku": "20_04-lts-gen2",
      "version": "latest"
    },
    "osDisk": {
      "caching": "ReadWrite",
      "createOption": "FromImage",
      "diffDiskSettings": {
        "option": ""
      },
      "diskSizeGB": "30",
      "encryptionSettings": {
        "enabled": "false"
      },
      "image": {
        "uri": ""
      },
      "managedDisk": {
        "id": "/subscriptions/35b0fa4f-b6ba-4752-87a9-d644b3f23b8b/resourceGroups/MyResourceGroup/providers/Microsoft.Compute/disks/myvm_disk1_14c1467024f349298ac0b1ecff9036be",
        "storageAccountType": "Premium_LRS"
      },
      "name": "myvm_disk1_14c1467024f349298ac0b1ecff9036be",
      "osType": "Linux",
      "vhd": {
        "uri": ""
      },
      "writeAcceleratorEnabled": "false"
    },
    "resourceDisk": {
      "size": "16384"
    }
  },
  "subscriptionId": "35b0fa4f-b6ba-4752-87a9-d644b3f23b8b",
  "tags": "",
  "tagsList": [],
  "userData": "",
  "version": "20.04.202305150",
  "vmId": "56cdefb2-0300-48a9-a9b6-883f2c828297",
  "vmScaleSetName": "",
  "vmSize": "Standard_D2s_v3",
  "zone": ""
}
som@myvm:~$ curl -s -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/curl -s -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | jq^Cpi-version
=2021-02-01" | jq
som@myvm:~$ curl -s -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/vmId?api-v
ersion=2021-02-01" | jq
{
  "error": "Bad request"
}
som@myvm:~$ exit
logout
Connection to 168.62.21.119 closed.

curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/privateIpAddress?api-version=2017-08-01&format=text"
curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/azEnvironment?api-version=2018-10-01&format=text"
curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/location?api-version=2018-10-01&format=text"
curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/name?api-version=2018-10-01&format=text"
curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/vmId?api-version=2017-08-01&format=text"
curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/vmSize?api-version=2017-08-01&format=text"
curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/subscriptionId?api-version=2017-08-01&format=text"

som@myvm:~$ curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/privateIpAddress?api-version=2017-08-01&format=text"
10.0.0.4som@myvm:~$ curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/azEnvironment?api-version=2018-10-01&format=text"
AzurePublicCloud
som@myvm:~$ curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/name?api-version=2018-10-01&format=text"
myvm
som@myvm:~$ curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/location?api-version=2018-10-01&format=text"
westus
som@myvm:~$ curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/vmId?api-version=2017-08-01&format=text"
56cdefb2-0300-48a9-a9b6-883f2c828297
som@myvm:~$ curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/vmSize?api-version=2017-08-01&format=text"
Standard_D2s_v3
som@myvm:~$ curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/subscriptionId?api-version=2017-08-01&format=text"
35b0fa4f-b6ba-4752-87a9-d644b3f23b8b
som@myvm:~$ logout
Connection to 168.62.21.119 closed.
PS C:\Users\somde\OneDrive\Desktop\PythonForDevops>