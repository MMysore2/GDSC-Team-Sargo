import streamlit as st
import pandas as pd 

dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.markdown(""""
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
st.markdown("**Here's our markdown**... *woahhh*")
#Insert link to markdown cheatsheet
st.markdown("[Link to Markdown cheatsheet](https://www.markdownguide.org/cheat-sheet/)")
st.latex(r"\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}")

#Inserting code into the app to display
json = {'name': 'John', 'age': '35', 'city': 'New York'}
code = '''def hello():
    print("Hello, Streamlit!")'''

st.json(json)
st.code(code, language='python')
st.error("This is an error")
st.warning("This is a warning")
st.info("This is a purely informational message")
st.success("This is a success message!")

st.write("This is a write function which allows us to do alot of things ")

st.write(dataframe)
st.write("Displays table using stwrite function")

st.table(dataframe)
st.write("Displays table as 'table'")

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
