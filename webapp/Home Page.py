import streamlit as st 
import joblib
import numpy as np
from PIL import Image


# To run the app with auto reload:
#streamlit run "Home Page.py" --server.runOnSave true 

# Include CSS files
def include_css(filename): 
    with open(filename, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def imageToArray(imageName):
  # Load the image and resize it to the desired dimensions
  image_path = '/content/drive/Shareddrives/TEAM SARGO/FindWaldo/Data/Train/'+ imageName + '.png'
  width, height = 64, 64  # Replace with the dimensions required by your model
  image = Image.open(image_path)
  image = image.resize((width, height))
  print(image.width)
  # Convert the image to a NumPy array and normalize the pixel values (if necessary)
  image_array = np.asarray(image)
  image_array = image_array / 255.0  # Normalize the pixel values between 0 and 1
  print(image_array.shape)
  # Reshape the image array to match the input shape of your model
  image_array = image_array.reshape(1, width, height, 3)  # Assumes the input shape is (width, height, 3)
  return image_array

def predict(image): 
    #Retrieve saved model from files
    model = joblib.load("static/model /final_model.pkl")
    
    #Make prediction
    prediction = model.predict(image)

    return prediction.toarray()



def main():
    # Page configuration
    st.set_page_config(
        page_title="Where's Waldo!",
        page_icon="static/img/waldo_icon.png",
        layout="wide",
        initial_sidebar_state="expanded",
        )

    #  Include header removal CSS files
    include_css('static/css/styles.css') 
    st.markdown("<center><h1> Let's Find Waldo! </h1></center>", unsafe_allow_html=True)
    st.markdown("<center><p> Begin by uploading an image of a Waldo pagebook or any other image containing Waldo <p><center>",unsafe_allow_html=True)
    uploadedImage = st.file_uploader("", type=["jpg", "png"])
    if uploadedImage: 
        st.success("Image uploaded!")
        st.image(uploadedImage)
        if st.button("Find Waldo!"):
            predict(uploadedImage)






        
if __name__ == "__main__":
    main()




