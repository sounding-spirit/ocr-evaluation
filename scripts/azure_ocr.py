import requests
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO
import os
import sys
import json
import glob
import time

indir = sys.argv[1]
outdir = sys.argv[2]

dirlist = []
dirlist = glob.glob(os.path.join(indir, '*.jpg'))

# Add your Computer Vision subscription key and endpoint to your environment variables.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

ocr_url = endpoint + "vision/v2.0/ocr"

for image in dirlist:
    image_path = image
    # Read the image into a byte array
    image_data = open(image_path, "rb").read()

    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    params = {'language': 'unk', 'detectOrientation': 'true'}
    #data = {'url': image_url}
    response = requests.post(ocr_url, headers=headers, params=params, data = image_data)
    response.raise_for_status()

    analysis = response.json()

    out = os.path.join(outdir, os.path.basename(image.rstrip('.jpg') + '.json'), )
    with open(out, 'w') as outfile:
        outfile.write(json.dumps(analysis))
        outfile.close()
    time.sleep(5)

# Extract the word bounding boxes and text.
# line_infos = [region["lines"] for region in analysis["regions"]]
# word_infos = []
# for line in line_infos:
#     for word_metadata in line:
#         for word_info in word_metadata["words"]:
#             word_infos.append(word_info)
# word_infos
