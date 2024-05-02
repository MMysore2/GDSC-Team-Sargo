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
    jacobRight.write("\nNice biograpghy")

    mysoreLeft, mysoreRight  = st.columns(2)

    #Insert path to the image you want here 
    mysore_pfp = mysoreLeft.image("../webapp/static/img/waldo_icon.png")

    mysoreRight.markdown("<center><h1> Mitha Mysore </h1></center>", unsafe_allow_html=True)
    mysoreRight.write("\nNice biograpghy about Mysore ")




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