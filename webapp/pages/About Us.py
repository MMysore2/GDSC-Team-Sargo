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
    MysoreLeft, jacobRight  = st.columns(2)

    #Insert path to the image you want here 
    jacob_pfp = MysoreLeft.image("../webapp/static/img/waldo_icon.png")

    jacobRight.markdown("<center><h1> Jacob Marinas </h1></center>", unsafe_allow_html=True)
    jacobRight.write("\nhi, I’m Jacob - 3rd year CS / Math @ UC Davis : ) a few facts about me:\ncame up here from Socal - I like experiencing and learning new things every day
previously did FTC / FRC robotics, game dev\nenjoy working on interesting / challenging problems with others - that’s why I’m here in GDSC : )\nalso a PM in CodeLab, working with the UC Davis Center for Educational Effectiveness (also CS Peer Advisor in training :o)\nother interests: cubing, rhythm games, dance, gym, tech, productivity\nfun fact: I’ve solved 9 Rubik’s Cubes in a row, blindfolded")

    mysoreLeft, mysoreRight  = st.columns(2)

    #Insert path to the image you want here 
    mysore_pfp = mysoreLeft.image("../webapp/static/img/waldo_icon.png")

    mysoreRight.markdown("<center><h1> Mitha Mysore </h1></center>", unsafe_allow_html=True)
    mysoreRight.write("\nHi! I’m Mysore! I’m a 3rd year CS major at UC Davis.\nWhen I’m not coding, you can find me drawing and crocheting! I also have two pet parakeets who love playing Minecraft with me.\nI took on this project to expand my toolkit, but it also taught me how to start a project from scratch. I hope to use what I learned to create more projects in the future!")




def main (): 

     # Include header removal CSS files
    include_css('static/css/styles.css') 
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
