#Link to the tutorial: https://www.youtube.com/watch?v=YQtH24_CCFs&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=10

import streamlit as st
import pandas as pd 

dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

#Editing a default Streamlit theme via inspect element/markdowns
st.markdown("""
<style>
.st-emotion-cache-ch5dnh.ef3psqc5
    {
        visibility: hidden;
    }   
</style>            
""", unsafe_allow_html=True)


st.title("Hello World! I am currently learning Streamlit.")
st.subheader("Here's our subheader")
st.header("Here's our header")
st.text("Here's our text")

#Inserting text and code in HTML is one feature of Streamlit
st.markdown("**Here's our markdown**... *woahhh*")
#Insert link to markdown/HTML cheatsheet
st.markdown("[Link to Markdown cheatsheet](https://www.markdownguide.org/cheat-sheet/)")

#Cool nice matrix thing
st.latex(r"\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}")

#Inserting code into the app to display
json = {'name': 'John', 'age': '35', 'city': 'New York'}
code = '''def hello():
    print("Hello, Streamlit!")'''
st.json(json)
st.code(code, language='python')

#Stuff 
st.error("This is an error")
st.warning("This is a warning")
st.info("This is a purely informational message")
st.success("This is a success message!")

#One of the best features in SL, the write function which allows us to display stuff easily 
st.write("This is a write function which allows us to do alot of things ")
st.write(dataframe)
st.write("Displays table using stwrite function")
st.table(dataframe)
st.write("Displays table as 'table'")

#Inserting media 
st.image("image.jpg", caption="This is an image! woahhhh", width=500, use_column_width=True)
st.audio("movie.mp3", format="audio/mp3")
st.video("Bruh.mp4", format="video/mp4")

#Logs changes in the checkbox to the console if needed 
def change(): 
    print("Changed:" + str(st.session_state.checker))

state = st.checkbox("Checkbox", on_change=change, key ="checker")
if state:
    st.write("Checkbox is checked")
else:
    st.write("Checkbox is unchecked")

#User input widgets
radio_button = st.radio("How are you feeling about finding Waldo?", ("Good", "Bad", "Ugly", "Why am I alive?"))
print(radio_button)

def button_click():
    print("Button was clicked")
button = st.button("Click me!", on_click=button_click)   

st.video("Cropped_9+10.mp4", start_time=0)
select = st.selectbox("What is the answer.....", options=[19, 21])
if select == 19:
    st.write("You're correct!")
elif select == 21:
    st.video("Cropped_9+10_2.mp4", format="video/mp4", start_time=5)

options = ["Crying", "Procrastinating", "Eating", "Sleeping", "Not Studying", "Using ChatGPT"]
multiselect = st.multiselect("What are some skills you have?", options=options)
st.write(multiselect)

#IMPORTANT: File uploading 
image = st.file_uploader("Upload a file", type=["jpg", "png"]) 
if image is not None:
    #Do whatever you want here 
    st.image(image, caption="Uploaded Image... woowwww", use_column_width=False)    

mult_images = st.file_uploader("Upload multiple files", type=["jpg", "png"], accept_multiple_files=True)
if mult_images is not None:
    #Do whatever you want here 
    for image in mult_images: 
        st.image(image, caption="Uploaded Image... woowwww", use_column_width=False)    


#More widgets for streamlit 

#Sliders 
slider_val = st.slider("This is a slider", min_value=0, max_value=100, value=0)
st.write(slider_val)

#Text input
text_input = st.text_input("This is a text input", value="Enter text here", max_chars=30)
print("You entered: ", text_input) 

paragraph = st.text_area("This is a text area", value="Enter text here", max_chars=100)
print("You entered a lovely paragraph: ", paragraph)

date_input = st.date_input("This is a date input", value=None)

small = st.number_input("This is a number input", value=0, step=1, format="%d")