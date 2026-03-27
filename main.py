import streamlit as st
from openai import OpenAI
import os

# 设置页面配置（必须放在最前面）
st.set_page_config(
    page_title="AI智能伴侣小皮",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 初始化 AI 客户端（只初始化一次）
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

print("---------> 重新执行此文件，渲染展示页面")

st.title("AI智能伴侣小皮")
st.logo("✨")

system_prompt = "你是一名非常可爱的AI助理，你的名字叫小皮，请你使用温柔可爱的语气回答用户的问题"

# 初始化聊天历史（修正拼写错误）
if "messages" not in st.session_state:
    st.session_state.messages = []

# 渲染历史消息
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

# 处理用户输入
prompt = st.chat_input("请输入您要问的问题")
if prompt:
    st.chat_message("user").write(prompt)
    print("---------> 请调用AI大模型，提示词：", prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用 DeepSeek API
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        stream=False
    )

    ai_response = response.choices[0].message.content
    print("<-------- 大模型返回的结果：", ai_response)

    st.chat_message("assistant").write(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})