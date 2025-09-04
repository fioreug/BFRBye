import sys
import base64


def imgToB64(img_name):

    with open(img_name, "rb") as img:
        s = base64.b64encode(img.read())
        #print(s)
        return s

img_name = sys.argv[1]
icon = imgToB64(img_name)
icon_file = f'icon = {icon}'

with open('icon.py', "w") as f:
    f.write(icon_file)