import streamlit as st
import requests


def convert_sketch_to_image(api_key, image, prompt):
    url = "https://api.stability.ai/v2beta/stable-image/control/sketch"
    
    files = {"image": image}
    data = {
        "prompt": prompt,
        "control_strength": 0.7,
        "output_format": "png"
    }
    
    headers = {
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    }
    
    response = requests.post(url, headers=headers, files=files, data=data)
    
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Error: {response.json()}")
        return None


st.title("sketch to image converter")


api_key = st.text_input("enter your stability AI API key", type="password")


uploaded_file = st.file_uploader("upload a sketch", type=["png", "jpg", "jpeg"])


prompt = st.text_input("enter a prompt", "a medieval castle on a hill")

if st.button("Convert Sketch"):
    if api_key:
        if uploaded_file is not None:
           
            image = convert_sketch_to_image(api_key, uploaded_file, prompt)
            
            if image:
                
                st.image(image, caption="generated image")
        else:
            st.error("please upload a sketch.")
    else:
        st.error("please enter your API key.")

