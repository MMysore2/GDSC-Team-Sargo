import streamlit as st 


# This will be our about us page

def getLinkedIn (profileName): 
    base_url = "https://www.linkedin.com/in/"
    linkedin_link = f'<a href="{base_url}{profileName}" target="_blank">Visit LinkedIn Profile</a>'
    return linkedin_link

st.set_page_config(
        page_title="About Us",
        page_icon="static/img/waldo_icon.png",
        layout="wide",
        initial_sidebar_state="expanded")

def display_members():
    col1, col2 = st.columns(2)
    jacob_pfp = col1.image("../webapp/static/img/waldo_icon.png")
    col2.markdown("<center><h1> Jacob Marinas </h1></center>", unsafe_allow_html=True)



def main (): 
    display_members()

# Mysore 

# Emma 

# Nelsen 

# Jacob
# Hi, I’m Jacob - 3rd year CS / Math @ UC Davis : ) a few facts about me:
# came up here from Socal - I like experiencing and learning new things every day
# previously did FTC / FRC robotics, game dev
# enjoy working on interesting / challenging problems with others - that’s why I’m here in GDSC : )
# also a PM in CodeLab, working with the UC Davis Center for Educational Effectiveness (also CS Peer Advisor in training :o)
# other interests: cubing, rhythm games, dance, gym, tech, productivity
# fun fact: I’ve solved 9 Rubik’s Cubes in a row, blindfolded





#Harjot 

if __name__ == "__main__":
    main()




# 