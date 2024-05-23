import streamlit as st 


# This will be our about us page

# Include CSS files
def include_css(filename): 
    with open(filename, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def getLinkedIn (profileName): 
    base_url = "https://www.linkedin.com/in/"
    linkedin_link = f'<a href="{base_url}{profileName}" target="_blank">Visit LinkedIn Profile</a>'
    return linkedin_link

st.set_page_config(
        page_title="About Us",
        page_icon="static/img/waldo_icon.png",
        layout="wide",
        initial_sidebar_state="expanded",
)

def display_members():
    jacobLeft, jacobRight  = st.columns(2)
    jacob_pfp = jacobLeft.image("../webapp/static/img/jacobPic.JPEG")
    jacobRight.markdown("<center><h1> Jacob Marinas </h1></center>", unsafe_allow_html=True)
    jacobRight.write("\nHi, I’m Jacob - a 3rd year CS / Math student at UC Davis. Here are a few facts about me:\nI came up here from SoCal and I enjoy experiencing and learning new things every day. \
                     I previously did FTC / FRC robotics and game development. I enjoy working on interesting and challenging problems with others, which is why I’m here in GDSC. \
                     I'm also a PM in CodeLab, working with the UC Davis Center for Educational Effectiveness. In my free time, I enjoy cubing, rhythm games, dance, gym, tech, and productivity. \
                     Fun fact: I’ve solved 9 Rubik’s Cubes in a row, blindfolded.")
    #New Line
    st.write("")
    mysoreLeft, mysoreRight = st.columns(2)
    mysore_pfp = mysoreLeft.image("../webapp/static/img/mysorePic.jpg")
    mysoreRight.markdown("<center><h1> Mitha Mysore </h1></center>", unsafe_allow_html=True)
    mysoreRight.write("\nHi! I’m Mysore! I’m a 3rd year CS major at UC Davis. When I’m not coding, you can find me drawing and crocheting! \
                      I also have two pet parakeets who love playing Minecraft with me. I took on this project to expand my toolkit, but it also taught \
                      me how to start a project from scratch. I hope to use what I learned to create more projects in the future!")
    #New Line
    st.write("")
    emmaLeft, emmaRight = st.columns(2)
    emma_pfp = emmaLeft.image("../webapp/static/img/emmaPic.jpg")
    emmaRight.markdown("<center><h1> Emma Chan </h1></center>", unsafe_allow_html=True)
    emmaRight.write("\nHi! I'm Emma and I'm a 3rd year CSE major at UC Davis. \
                    In my free time, I enjoy composing music, building in Minecraft, and various other hobbies! \
                    I joined GDSC to gain valuable project experience and expand my CS knowledge :D")
    
    #New Line
    st.write("")
    harjotLeft, harjotRight = st.columns(2)
    harjot_pfp = harjotLeft.image("../webapp/static/img/harjotPic.jpg")
    harjotRight.markdown("<center><h1> Harjot Gill </h1></center>", unsafe_allow_html=True)
    harjotRight.write("\nHello all. Thank you for checking out our project! I am a 3rd year CS major at UC Davis. Some of my hobbies include driving, basketball and more! \
                      I have always been a car enthusiast and enjoy anything automotive! \
                      I joined GDSC initially to get some hands-on experience with projects and stayed for my amazing team!")

    #New Line
    st.write("")
    nelsenLeft, nelsenRight = st.columns(2)
    nelsen_pfp = nelsenLeft.image("../webapp/static/img/nelsenPic.jpg")
    nelsenRight.markdown("<center><h1> Nelsen Young </h1></center>", unsafe_allow_html=True)
    nelsenRight.write("\n Example")


def main (): 

     # Include header removal CSS files
    include_css('static/css/styles.css') 
    display_members()

# Nelsen 

if __name__ == "__main__":
    main()




# 
