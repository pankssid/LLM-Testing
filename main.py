import streamlit as st
import random
import time
import requests

st.set_page_config(layout="wide")
st.title("Multilingual ChatBot")



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Say something in English/Spanish/Arabic"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        def model_api(prompt):
            # if st.button("Submit"):
            API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
            headers = {"Authorization": "Bearer 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"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.json()
                
            output = query({
                "inputs":prompt,
            })

            return output[0]['generated_text']


        assistant_response = model_api(prompt)
        
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})





# import streamlit as st

# import base64
# import requests

# # def ad_bg_from_local(image_file):
# #     with open(im)
# # Setting the page layout 
# st.set_page_config(layout="wide")

# #######  Code to set the theme and Background ########
# # def add_bg_from_local(image_file):
# #     with open(image_file, "rb") as image_file:
# #         encoded_string = base64.b64encode(image_file.read())
# #     st.markdown(
# #     f"""
# #     <style>
# #     .stApp {{
# #         background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
# #         background-size: cover
# #     }}
# #     </style>
# #     """,
# #     unsafe_allow_html=True
# #     )
# # add_bg_from_local('image/mlai_digital.png')


# def main():

#     # st.title("")
#     # Display or clear chat messages
#     # for message in st.session_state.messages:
#     #     with st.chat_message(message["role"]):
#     #         st.write(message["content"])
   
#     user_input= st.text_input("Enter your question in English/Spanish/Arabic ")


#     if st.button("Submit"):
#         API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
#         headers = {"Authorization": "Bearer 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"}

#         def query(payload):
#             response = requests.post(API_URL, headers=headers, json=payload)
#             return response.json()
            
#         output = query({
#             "inputs":user_input,
#         })
#         st.write(output[0]['generated_text'])
#         # Print or do something with the values
#         # for key, value in input_values.items():
#         #     st.write(f"{key}: {value}")

#     # st.write(Template_2)
# if __name__ == "__main__":
#     main()
