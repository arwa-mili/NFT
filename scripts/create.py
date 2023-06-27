import requests
import os
import json

def main():
    token_metadata = dict()

    # Store the token's metadata locally in this file
    meta_data_file = "metadata/data.json"
    
    # Name of the token
    token_metadata["name"] = "<NAME OF YOUR TOKEN>"
    # Description of the token
    token_metadata["description"] = "<DESCRIPTION OF YOUR TOKEN>"

    # Path of the artwork to be uploaded to IPFS
    image_path = "images/image.jpg"
    with open(image_path, "rb") as f:
        image_data = f.read()

    # Upload the image to IPFS and get the storage address
    image = upload(image_data)
    
    # Add the image URI to the metadata
    image_path = f"https://ipfs.io/ipfs/{image}"
    token_metadata["image"] = image_path
    print(token_metadata)

    with open(meta_data_file, "w") as f:
        json.dump(token_metadata, f)

    # Convert dictionary to bytes
    encoded_data = json.dumps(token_metadata).encode('utf-8')

    # Upload the metadata of token to IPFS
    meta_data_hash = upload(encoded_data)

    # Write the metadata URI to a file
    meta_data_path = f"https://ipfs.io/ipfs/{meta_data_hash}"
    with open('metadata/metadata.json', 'w') as f:
        json.dump(meta_data_path, f)
    return 0

def upload(data):
    # Get Pinata credentials from the .env file
    pinata_api_key = os.environ["PINATA_API_KEY"]
    pinata_api_secret = os.environ["PINATA_API_SECRET"]
    endpoint = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {
        'pinata_api_key': pinata_api_key,
        'pinata_secret_api_key': pinata_api_secret
    }
    body = {
        'file': data
    }
    # POST the pin request to Pinata
    response = requests.post(endpoint, headers=headers, files=body)
    
    # Return the IPFS hash where the data is stored
    return response.json()["IpfsHash"]