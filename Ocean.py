import google.generativeai as genai
import PIL.Image

img = PIL.Image.open('e:\my documents\my document\WhatsApp Image 2024-04-24 at 20.14.27_eca7a31d.jpg')

genai.configure(api_key='')

model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(["which object are there in this image", img])

print(response.text)
