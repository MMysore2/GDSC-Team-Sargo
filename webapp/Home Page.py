import streamlit as st 

# To run the app with auto reload:
#streamlit run "Home Page.py" --server.runOnSave true 

# Include CSS files
def include_css(filename): 
    with open(filename, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    # Page configuration
    st.set_page_config(
        page_title="Where's Waldo!",
        page_icon="static/img/waldo_icon.png",
        layout="wide",
        initial_sidebar_state="expanded")

     # Include header removal CSS files
    include_css('static/css/styles.css') 

    #Side bar containing webpages 
    sidebar()



def sidebar():
    # ******Sidebar of the page*****
    with st.sidebar:
        # st.markdown("<center><h1></h1></center>", unsafe_allow_html=True)
        st.write("Hi")


        
if __name__ == "__main__":
    main()




