import streamlit as st
import anthropic

st.title("📝 File Q&A with Anthropic")
uploaded_file = st.file_uploader("Upload an article", type="pdf")
question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

if uploaded_file and question:
    article = uploaded_file.read().decode()
    prompt = f"""{anthropic.HUMAN_PROMPT} Here's an article:\n\n<article>
    {article}\n\n</article>\n\n{question}{anthropic.AI_PROMPT}"""

    client = anthropic.Client(st.secrets.anthropic_api_key)
    response = client.completion(
        prompt=prompt,
        stop_sequences=[anthropic.HUMAN_PROMPT],
        model="claude-v1",
        max_tokens_to_sample=100,
    )
    st.write("### Answer")
    st.write(response["completion"])
