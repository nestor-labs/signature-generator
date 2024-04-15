import base64

with open("signature.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

print(encoded_string.decode("utf-8"))
