from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import os
import streamlit as st
from pydantic import SecretStr

load_dotenv()

llm = ChatOpenAI(
    model="DeepSeek-V4-Flash-0731",
    api_key=SecretStr(os.environ["API_KEY"]),
    base_url="https://routesme.online/v1",
)

# Prompt template with variables: paper_name, style, length


st.header("Research Tool")

paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

prompt_templates = load_prompt('prompt_template.json')

if st.button('Summarize'):
    if paper_input and style_input and length_input:
        with st.spinner("Thinking..."):
            chain = prompt_templates | llm
            result = chain.invoke({
            "paper_name": paper_input,
            "style": style_input,
            "length": length_input,
        })
            
        st.write(result.content)
    else:
        st.warning("Please select all options before summarizing.")
