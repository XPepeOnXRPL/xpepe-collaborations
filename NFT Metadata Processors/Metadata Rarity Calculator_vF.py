import json
import glob
from collections import defaultdict

try:
    # Load the metadata from a bunch of json files in a folder called metadata
    nfts = []
    # Adjust this to the path where your JSON files are located
    for filename in glob.glob('metadata/*.json'):
        with open(filename, 'r') as f:
            nft = json.load(f)
            nft['filename'] = filename  # Store the filename with the NFT
            nfts.append(nft)

    # Calculate the count of each trait value across all NFTs
    trait_value_counts = defaultdict(int)
    for nft in nfts:
        for attribute in nft['attributes']:
            key = (attribute['trait_type'], attribute['value'])
            trait_value_counts[key] += 1

    # Calculate the rarity of each attribute of each NFT based on the counts calculated above
    for nft in nfts:
        for i in range(len(nft['attributes'])):
            attribute = nft['attributes'][i]
            key = (attribute['trait_type'], attribute['value'])
            attribute['rarity'] = 1 / trait_value_counts[key]
            nft['attributes'][i] = attribute

        # Calculate the average rarity of each NFT
        total_rarity = sum(attribute['rarity'] for attribute in nft['attributes'])
        nft['rarity'] = total_rarity / len(nft['attributes'])

    # Sort the NFTs by rarity and assign a rank to each NFT
    nfts.sort(key=lambda nft: nft['rarity'])  # Sort in descending order of rarity
    for i, nft in enumerate(nfts, start=1):
        nft['rank'] = i

    # Save the updated NFT metadata back to the JSON file
    for nft in nfts:
        with open(nft['filename'], 'w') as f:
            # Remove the filename from the NFT before saving, because it's not part of the original metadata
            nft.pop('filename')
            json.dump(nft, f)

    print("Metadata rarity calculation and ranking completed successfully.")
except Exception as e:
    print("An error occurred during metadata rarity calculation and ranking:")
    print(str(e))
