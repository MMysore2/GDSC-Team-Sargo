import streamlit as st 
# To run the app with auto reload:
#streamlit run app.py --server.runOnSave true

# Include CSS files
def include_css(filename): 
    with open(filename, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
     # Include header removal CSS files
    include_css('static/css/styles.css') 


if __name__ == "__main__":
    main()