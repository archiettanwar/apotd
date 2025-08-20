import requests
import streamlit as st

st.set_page_config(layout="wide")

url=("https://api.nasa.gov/planetary/"
     "apod?"
     "api_key=7iUsZAtSHo6Zr4UV6RiWUMmZLJOuQiDPMHeEBD7O")

response=requests.get(url)
content=response.json()
print(content)
print(content["title"])
print(content["explanation"])
print(content["date"])

img_url=content["url"]
response2=requests.get(img_url)
img_path="image.jpeg"
with open(img_path,"wb") as file:
    file.write(response2.content)

st.title(f"{content["title"]}")
st.image(f"{img_path}")
st.write(f"{content["explanation"]}")