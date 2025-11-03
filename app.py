from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import streamlit as st
import os

st.title("AI専門家に相談しよう!")

st.write("選択した専門家としてAIが回答します!")
st.write("### ①転職の専門家")
st.write("### ②健康の専門家")
st.write("入力フォームにテキストで質問を入力し、「実行」ボタンを押すことで回答が得られます!")

selected_item = st.radio(
    "どちらの専門家に相談するか選択してください。",
    ["転職の専門家", "健康の専門家"]
)

st.divider()

user_input = st.text_input("質問を入力してください：")

if st.button("実行"):
    if not user_input:
        st.warning("質問を入力してください。")

    else:
        if selected_item == "転職の専門家":
            system_message = SystemMessage(
            content="あなたは転職の専門家です。ユーザーの質問に対して、的確で親切なアドバイスを提供してください。"
        )
        else:
            system_message = SystemMessage(
            content="あなたは健康の専門家です。ユーザーの質問に対して、的確で親切なアドバイスを提供してください。"
        )

    human_message = HumanMessage(content=user_input)

    chat = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.5,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    response = chat([system_message, human_message])

st.divider()

st.write("### 回答:")
st.write(response.content)