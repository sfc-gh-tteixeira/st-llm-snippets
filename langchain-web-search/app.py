import streamlit as st
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

st.title("🔎 Search with LangChain")
question = st.text_input("What do you want to know?", placeholder="Who won the Women's U.S. Open in 2018?")

llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=st.secrets.openai_api_key)
search = GoogleSerperAPIWrapper(serper_api_key=st.secrets.serper_api_key)
search_tool = Tool(
    name="Intermediate Answer",
    func=search.run,
    description="useful for when you need to ask with search",
)
search_agent = initialize_agent([search_tool], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

if question:
    response = search_agent.run(question)
    st.write("### Answer")
    st.write(response)
