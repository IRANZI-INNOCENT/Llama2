import streamlit as st
from langchain_community.llms import CTransformers
from langchain.prompts import PromptTemplate

# Load the LLaMA 2 model during app initialization
@st.cache(allow_output_mutation=True)
def load_model():
    llm = CTransformers(model='IranziInnocent/llama-2-7b-chat.ggmlv3.q8_0',
                        model_type='llama',
                        config={'max_new_tokens': 256, 'temperature': 0.01})
    return llm

# Function to get response from LLaMA 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    llm = load_model()  # Ensure the model is loaded
    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
    """
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template=template)
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    return response

# Streamlit UI code
st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generative AI 🤖")

input_text = st.text_input("Enter a Topic")

# Creating two more columns for additional 2 fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Target', ('Researchers', 'Data Scientist', 'Common People'), index=0)
    
submit = st.button("Generate")

# Final response
if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))

st.markdown('Developed By: IRANZI INNOCENT')
