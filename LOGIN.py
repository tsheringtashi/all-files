import streamlit as st
from PIL import Image

st.markdown('<link rel = "stylesheet" href = "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity')
st.markdown("""
<nav class="nav">
  <a class="nav-link active" aria-current="page" href="#">Active</a>
  <a class="nav-link" href="#">Link</a>
  <a class="nav-link" href="#">Link</a>
  <a class="nav-link disabled">Disabled</a>
</nav>
""", unsafe_allow_html=True)

# img = Image.open("D:/DHI_GIC/pic/logo.png")
st.set_page_config(page_title= "DCIC APP")

img1, img2 , img3= st.columns([10,1,10])


st.markdown("##")


contact_form = """
<form action="https://formsubmit.co/tashinus@email.com" method="POST">
     <input type="hidden" name="_captcha"value="false">
     <input type="email" name="email" placeholder = "Your email or userid" required>
     <input type="password" name="password" placeholder ="password" required>
     <button type="submit">Sign in</button> <button type="submit">Sign up</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# use local css file

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

local_css("style/login.css")

