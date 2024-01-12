# NFT Metadata Processing Tool

This repository contains two scripts for processing NFT metadata. The first script calculates the rarity of each attribute across all NFTs, and the second script merges individual metadata files into a single file.

## File 1: Rarity Calculator

### Description

This script loads metadata from a series of JSON files in a folder named `metadata`. It then calculates the rarity of each attribute and assigns a rank to each NFT based on this rarity. Finally, it updates the NFT metadata back to the JSON files.

### Usage

- Ensure your JSON files are located in a folder named `metadata`.
- Run the script.

### Features

1. Load NFT metadata from JSON files.
2. Calculate the count of each trait value across all NFTs.
3. Calculate the rarity of each attribute.
4. Calculate the average rarity of each NFT.
5. Sort NFTs by rarity and rank them.
6. Save the updated metadata back to the original JSON files.

## File 2: Metadata Merger

### Description

This script reads individual metadata files from the `./metadata` folder, merges them, and then writes the merged data to a single `metadata.json` file.

### Usage

- Ensure your metadata files are located in the `./metadata` directory.
- Run the script.

### Features

1. Read individual metadata files.
2. Merge individual metadata files into a combined list.
3. Adjust the image link for each NFT.
4. Write the merged metadata to a single `metadata.json` file.

---

Note: Always backup your data before running any scripts to prevent any unwanted modifications or data loss.

