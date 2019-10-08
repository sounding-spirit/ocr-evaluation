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

# Get positional text data
print '\t'.join(['x', 'y', 'w', 'h', 'content'])
with open(file, 'r') as f:
    data = json.loads(f.read())
    for blob in data['recognitionResults']:
        for line in blob['lines']:
            for word in line['words']:
                '''
                Example:
                {u'boundingBox': [2467, 2791, 2593, 2794, 2591, 2837, 2465, 2835], u'text': u'James.'}
                '''
                coordinates = word['boundingBox']
                x = int(coordinates[0])
                y = int(coordinates[1])
                lower_x = int(coordinates[4])
                lower_y = int(coordinates[5])
                w = abs(x-lower_x)
                h = abs(y-lower_y)
                content = word['text'].encode('utf8')

                print '\t'.join([str(x), str(y), str(w), str(h), content])
