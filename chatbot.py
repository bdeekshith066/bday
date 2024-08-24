import streamlit as st

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
        <div class="gradient-text">Nostalgia Narrator</div>
        """

  
    st.markdown(gradient_text_html, unsafe_allow_html=True)
    

    st.write(" Explore Nostalgia Narrator with me.  \n \n Dive into our shared :orange[experiences], rediscover treasured :orange[moments], and celebrate the :orange[bonds] that shape our lives. Happy Birthday, and here’s to :orange[many more memories!]")
    

    st.markdown(
    """
    <style>
    .stButton button {
        background-color: #6A5ACD; /* Light Slate Blue color */
        color: white;
        border-radius: 6px;
        padding: 8px 16px;
        font-size: 14px;
        font-family: 'Arial', sans-serif; /* Stylish font */
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #836FFF; /* Lighter shade on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)


    with st.form('Question1'):
        st.write(" :orange[1].  Still remember the day we met, it was as if the universe had conspired to bring us together.  We struck up a conversation, and I knew in that instant that I wanted to spend more time with you. What was the date that changed my life forever?")

        if st.form_submit_button("Missed It? Hint Inside! 🎁"):
            st.write("Enter the date in dd/mm/yy")

    with st.form('Question2'):
        st.write(" :orange[2]. Think about our happiest moments together. What is the one word that best captures the joy and laughter we've shared?")
        if st.form_submit_button("Missed It? Hint Inside! 🎁"):
            st.write("Enter one word")



    with st.form('Question3'):
        st.write(" :orange[3]. Reflecting on our occasional disagreements, what's the one word that describes how we've always managed to overcome them?")
        if st.form_submit_button("Missed It? Hint Inside! 🎁"):
            st.write("Enter one word")

    
    with st.form('Question4'):
        st.write(" :orange[4]. Looking ahead to the future, what one word best describes what you hope for us as we continue our journey together?")
        if st.form_submit_button("Missed It? Hint Inside! 🎁"):
            st.write("Enter one word")





    st.write('')
    st.write('')

    st.write('')
    st.write('')

    st.write('')
    st.write('')
    st.write('')

    def get_fest_info(user_input):
        fest_info = {
           

            "05/06/2024": """ That day is etched in my heart, a moment when everything aligned perfectly—the universe whispered, and our paths crossed. I remember the spark, the instant connection, the way my world shifted. That day wasn't just any day; it was the day everything changed, the day you walked into my life and turned it into a beautiful journey.""",
            "joy": "Every happy moment we've shared has been filled with pure joy. From our spontaneous adventures to the little everyday laughs, these memories are the heart of our bond. It's the joy that has made our journey together so special and unforgettable.",
            "understanding": "Despite our occasional disagreements, our understanding and ability to communicate openly have always brought us back together. It's this understanding that has strengthened our relationship and helped us grow closer.",
            "growth": "As we look to the future, my hope is for our continued growth together. It’s the growth that will bring new experiences, strengthen our bond, and help us build a future filled with shared dreams and achievements."


            

            
        }

        user_input_lower = user_input.lower()

        for fest, info in fest_info.items():
            if fest == user_input_lower:
                return info

        return "Oops! That’s not quite right. Maybe the hint could help? ❤️ Give it another try!"

    

    if "fest_messages" not in st.session_state:
        st.session_state.fest_messages = [{"role": "assistant", "content": "Answer the following questions in order"}]

    for message in st.session_state.fest_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter the answer in specified format"):
        st.session_state.fest_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = get_fest_info(prompt)

        with st.spinner(text="Thinking..."):
            st.session_state.fest_messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.write(response, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
