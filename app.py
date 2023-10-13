import streamlit as st

model_set = {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        }

st.title("トークン・カウントあぷり")

llm_model = st.selectbox('モデルを選んで下さい：', model_set)

col1, col2 = st.columns(2)
with col1:
    text_1 = st.text_area()
with col2:
    st.metric(value="tokens")

if st.button("トークンをカウント", type="primary"):
    tokens = num_tokens_from_messages(text_1, llm_model)

if tokens:
    st.metric(value = tokens)
