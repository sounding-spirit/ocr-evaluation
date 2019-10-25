import boto3
import sys

page = sys.argv[1]

client = boto3.client('textract')

response = client.detect_document_text(Document = {'Bytes': open(page, 'rb').read()})

# Print the plain text out line by line
for block in response['Blocks']:
    if block['BlockType'] == 'LINE':
        print(block['Text'])
