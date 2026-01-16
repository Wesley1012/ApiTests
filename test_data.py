import os
import base64

with open("tests/images/image.jpg", "rb") as image:
    image64 = base64.b64encode(image.read()).decode('utf-8')

with open("tests/images/avatar.jpeg", "rb") as image:
    avatar64 = base64.b64encode(image.read()).decode('utf-8')

path_photo = os.path.join(os.path.dirname(__file__), 'tests/images/image.jpg')
photo = (path_photo, open(path_photo, 'rb'), 'image/jpeg')