from PIL import Image
import requests
import json
import io
import random
url='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=ZKxajZngwxvtKfbneWUu2QvF1YUTWf22h8k3KPgm'
res=requests.get(url).json()
print(random.choice(res['photos']))


