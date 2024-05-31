import streamlit as st 


# This will be our about us page

# Include CSS files
def include_css(filename): 
    with open(filename, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.set_page_config(
        page_title="About The Project",
        page_icon="static/img/waldo_icon.png",
        layout="wide",
        initial_sidebar_state="expanded",
)

def main (): 

     # Include header removal CSS files
    include_css('static/css/styles.css') 
    githubLink, makesense, tensorflow, colab, = st.columns(4)
    githubLink.markdown("""<a href="https://github.com/MMysore2/GDSC-Team-Sargo">
                                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="100">
                                </a>
                                """,
                                unsafe_allow_html=True)
    makesense.markdown("""<a href="https://www.makesense.ai/">
                                <img src="https://www.makesense.ai/ico/main-image-color.png" width="150">
                                </a>
                                """,
                                unsafe_allow_html=True)
    
    tensorflow.markdown("""<a href="https://www.tensorflow.org/">
                                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/1200px-Tensorflow_logo.svg.png" width="100">
                                </a>
                                """,
                                unsafe_allow_html=True)
    
    colab.markdown("""<a href="https://colab.research.google.com/drive/">
                                <img src="https://res.cloudinary.com/startup-grind/image/upload/c_fill,w_500,h_500,g_center/c_fill,dpr_2.0,f_auto,g_center,q_auto:good/v1/gcs/platform-data-dsc/events/Google_Colaboratory_SVG_Logo.svg.png" width="130">
                                </a>
                                """,
                                unsafe_allow_html=True)
    
    st.write("")
    st.write("  Being a ML project, we need to use several libraries and resources including  \
                        Tensorflow to train the model, \
                        MakeSense.Ai for image annotation, \
                        Google Colab for a development environment, \
                        The model itself (Keras CNN), and \
                        Streamlit and CSS for the website") 
                    
# Nelsen 

if __name__ == "__main__":
    main()

