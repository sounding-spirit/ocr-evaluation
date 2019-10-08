import sys
import json

file = sys.argv[1]

# Remove extra json objects
with open(file, 'r') as f:
    lines = f.readlines()
with open(file, 'w') as f:
    for line in lines:
        if line.strip('\n') != '{"status": "Running"}':
            f.write(line)
    f.close()

# Get plain text
with open(file, 'r') as f:
    data = json.loads(f.read())
    for blob in data['recognitionResults']:
        for line in blob['lines']:
            print line['text']
