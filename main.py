import requests
import streamlit as st

st.set_page_config(layout="wide")

url=("https://api.nasa.gov/planetary/apod?"
     "api_key=B1QDrTTToXr5zj9ehEL21qS9Qnx1nW1BqA8fOLvL")

response=requests.get(url)
content=response.json()
print(content)
print(content["title"])
print(content["explanation"])
print(content["date"])
print(content["copyright"])

col1,col2=st.columns(2)

img_url=content["url"]
response2=requests.get(img_url)
img_path="image.jpeg"
with open(img_path,"wb") as file:
    file.write(response2.content)



with col1:
    st.title(f"{content["title"]}")
    st.image(f"{img_path}")

with col2:
    st.write(f"{content["date"]}")
    st.write(f"{content["copyright"]}")

st.write(f"{content["explanation"]}")

