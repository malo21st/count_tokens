import streamlit as st

tokens = 0
model_set = {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        }

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
    """Return the number of tokens used by a list of messages."""
    count = len(messages)
    return count

# view
st.title("トークン・カウントあぷり")

llm_model = st.selectbox('モデルを選んで下さい：', model_set)

col1, col2 = st.columns(2)
with col1:
    text_1 = st.text_area("入力して下さい：")
with col2:
    result = st.empty()

if st.button("トークンをカウント", type="primary"):
    tokens = num_tokens_from_messages(text_1, llm_model)
    result.metric(label="カウント結果：", value=f"{tokens} tokens")
