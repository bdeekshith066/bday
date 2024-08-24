import streamlit as st
import time
import io

def app():
    gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 2.25em;
        }
        </style>
        <div class="gradient-text">Happy Birthday Name</div>
        """
    #while taking input of name what u have to do is if user enteres name more than 9 letter then birthday should be bday in order to accomodate everything in one line otherwise the ui part wont look good in phone...
    
    
    st.markdown(gradient_text_html, unsafe_allow_html=True)
    # this should also be around 35 characters max i will let uk..as of now keep max as 35 characters and then when they exceed a small message should get displayed keep it short for better readabiltiy
    st.write(" :orange[A true friend with a heart of gold 💛 and endless joy 😊]")

    def typewriter(text: str, speed: int):
            tokens = text.split()
            container = st.empty()
            for index in range(len(tokens) + 1):
                curr_full_text = " ".join(tokens[:index])
                container.markdown(curr_full_text)
                time.sleep(1 / speed)

#Sample Example
    text = """ Happy birthday to an amazing person! 🎉🎂. Your infectious laughter 😂 and unwavering support 🙌 have made life’s journey so much sweeter. I hope your day is filled with love, laughter, and all your favorite things. 🎁🍰 May this new year bring you incredible adventures, unforgettable memories, and endless joy. Here's to an incredible year ahead! 🥳🎊 Here’s to another year of amazing memories together!  May our paths cross soon and we can celebrate in person! 🤗 """
    speed = 3
    typewriter(text=text, speed=speed)

    #since we are uploading on github the max file size should be kept in mind also we will have to reduce the file size if it exceeds the limit...
    #give option of audio also in the form...audio of they wishing happy birthday or they laying soome instruments....
    st.write('')

    st.write(':orange[Listen to this 🎧—a heartfelt birthday wish just for you.]')
    audio_file = open('audio.mp3', 'rb')
    audio_bytes = audio_file.read()



    
    st.audio(io.BytesIO(audio_bytes))
    video_file = open('videoo.mp4', 'rb')
    video_bytes = video_file.read()

    time.sleep(15)
    st.write('')

    st.write(":orange[Watch this short video 🎥—a glimpse into our incredible journey together.]")

    st.video(video_bytes)


    st.write('')
    st.write('')
    st.write('Think this is it? 🎁 There’s more to discover! Head to the top left corner for extra surprises')


    #for this page u will be taking input of name , one liner about the person , bday wishing message , video , audio
