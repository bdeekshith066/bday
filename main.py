import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
import streamlit.components.v1 as components


import  home, chatbot, lastpage

# Reducing whitespace on the top of the page
st.markdown("""
<style>

.block-container
{
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)









class MultiApp:
    def __init__(self):
        self.app = []

    def add_app(self, title, func):
        self.app.append({
            "title": title,
            "function": func
        })   

    def run(self):  
        with st.sidebar:
            
           
            st.markdown("""
          <style>
            .gradient-text {
              margin-top: -20px;
            }
          </style>
        """, unsafe_allow_html=True)
            
            typing_animation = """
            <h3 style="text-align: left;">
            <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=48&Left=true&vLeft=true&width=500&height=70&lines=🍾HBD+nickname" alt="Typing Animation" />
            </h3>
            """
            st.markdown(typing_animation, unsafe_allow_html=True)
            
            app = option_menu(
                menu_title='Sections',
                options=['Home','Nostalgia Narrator', 'idkkk'],
                default_index=0,
            )
            st.write('')
            st.write('')
            st.write('')

            components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
  margin: 0; /* Remove default margin */
  padding: 0; /* Remove default padding */
}
body {
  font-family: Verdana, sans-serif;
}
.mySlides {
  display: none;
}
img {
  vertical-align: middle;
  width: 100%; /* Make images fill their containers */
  margin: 0; /* Remove any margin */
  padding: 0; /* Remove any padding */
}
/* Slideshow container */
.slideshow-container {
  max-width: 300px;
  max-height : 300px;
  position: 100%;
  margin: 0;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}
/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.5s;
}
@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
</style>
</head>
<body>
<div class="slideshow-container">
  <div class="mySlides fade">
    <div class="numbertext">1 / 3</div>
    <img src="https://plus.unsplash.com/premium_photo-1663839412026-51a44cfadfb8?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8YmlydGhkYXl8ZW58MHx8MHx8fDA%3D">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">2 / 3</div>
    <img src="https://ih0.redbubble.net/image.4989446811.4229/raf,360x360,075,t,fafafa:ca443f4786.jpg">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">3 / 3</div>
    <img src="https://unsplash.com/photos/zVhYcSjd7-Q/download?force=true&w=1920">
    
  </div>
</div>
<script>
  let slideIndex = 0;
  showSlides();

  function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    slides[slideIndex-1].style.display = "block";  
    setTimeout(showSlides, 2000); // Change image every 2 seconds
  }
</script>
</body>
</html>
    """,
    height=200, width=300
)
            
           
            
            
        if app == "Home":
            home.app()
        
        elif app == 'Nostalgia Narrator':
            chatbot.app()
        
        elif app == 'idkkk':
            lastpage.app()

        
            

# Create an instance of the MultiApp class and run the app
MultiApp().run()
