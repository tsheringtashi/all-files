import streamlit as st
from PIL import Image

# img = Image.open("D:/DHI_GIC/pic/logo.png")
st.set_page_config(page_title= "DCIC APP")

img1, img2, img3,img4, img5, img6,img7 = st.columns(7)
# img3.image(img)
st.header(":lock:")

contact_form = """
<form action="https://formsubmit.co/tashinus@email.com" method="POST">
     <input type="hidden" name="_captcha"value="false">
     <input type="text" name="userid" placeholder ="userid" required>
     <input type="email" name="email" placeholder = "your email" required>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# use local css file

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

local_css("style/style.css.css")

st.markdown("#")
st.markdown("#")
st.markdown(":cool: DHI Companies Integrated Communication System developed by Team BoB.")