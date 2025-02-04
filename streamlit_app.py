import streamlit as st
import requests

# Set the page title
st.set_page_config(page_title="Virtual Tutor")

# Add a title to the app
st.title("Virtual Tutor")

# # Read the base URL from a local text file
# def get_base_url():
#     try:
#         with open("base_url.txt", "r") as file:
#             return file.read().strip()
#     except FileNotFoundError:
#         st.error("Base URL file not found. Please ensure 'base_url.txt' exists in the app directory.")
#         return None

base_url  = "https://ai-lab.hydra-agama.vip/"

# Create a text area for user input
user_input = st.text_area("Enter your query:", "", height=150)

# Add a button
if st.button("Query"):
    # Handle the button click
    if user_input.strip():
        if base_url:
            try:
                # Perform the GET request
                response = requests.get(
                    f"{base_url}/webhook-test/be62a745-b5c9-40b0-b6b0-284fb72bc1d9",
                    params={"query": user_input},
                    headers={"X-TOKEN": "akMAHGaeJKuMTIziibMBYHIg"}
                )
                if response.status_code == 200:
                    # Extract and display the 'Answer' field from the JSON response
                    answer = response.json().get("response").get("text", "No answer provided.")
                    st.success(answer)
                else:
                    st.write("Failed to fetch the answer. Please try again later.")
            except Exception as e:
                st.write(f"An error occurred: {e}")
        else:
            st.write("Cannot query without a valid base URL.")
    else:
        st.write("Please enter a paragraph to query.")

# Display the version number at the bottom of the app
st.markdown("---")
st.text("Version: 1.1")
