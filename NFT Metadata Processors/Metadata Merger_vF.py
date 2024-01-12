import os
import json

FOLDER = './metadata'
result = []


def read_files():
    try:
        print('Reading files...')
        json_files = [f for f in os.listdir(FOLDER) if f.endswith('.json')]
        print(f'Found {len(json_files)} files.')
        return json_files
    except FileNotFoundError:
        print(f'Error: Folder "{FOLDER}" not found.')
        return []


def merge_files(json_files):
    try:
        print('Merging...')
        json_files.sort(key=lambda x: int(x.split('.')[0]))

        for idx, f in enumerate(json_files):
            with open(os.path.join(FOLDER, f)) as json_file:
                data = json.load(json_file)
                data['image'] = 'ipfs://bafybeihfzizevrwgdgucrtc23mrlmzdy4d35dljf6vutp2bgegpvdqkypa/' + str(
                    idx + 1) + '.png'
                result.append(data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error: {str(e)}')


def write_output():
    try:
        print('Writing output...')
        with open('metadata.json', 'w') as outfile:
            json.dump(result, outfile)
        print('Done.')
    except PermissionError:
        print('Error: Permission denied. Failed to write output file.')


def main():
    json_files = read_files()
    if json_files:
        merge_files(json_files)
        write_output()


if __name__ == "__main__":
    main()
