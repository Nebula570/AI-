import streamlit as st
from openai import OpenAI
import os
#设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣小皮",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

print("---------> 重新执行此文件，渲染展示页面")



st.title("AI智能伴侣pp")

st.logo("✨")

system_prompt="你是一名非常可爱的AI助理，你的名字叫小皮，请你使用温柔可爱的语气回答用户的问题"

if "massages" not in st.session_state:
    st.session_state.massages = []

for massage in st.session_state.massages:
    if massage["role"] == "user":
        st.chat_message("user").write(massage["content"])
    else:
        st.chat_message("assistant").write(massage["content"])



client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")


prompt=st.chat_input("请输入您要问的问题")
if prompt:
    st.chat_message("user").write(prompt)
    print("---------> 请调用AI大模型，提示词：",prompt)
    st.session_state.massages.append({"role":"user","content":prompt})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system",
             "content": system_prompt},
             *st.session_state.massages
        ],
        stream=False
    )

    print("<-------- 大模型返回的结果：",response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    st.session_state.massages.append({"role":"assistant","content":response.choices[0].message.content})

































