import streamlit as st
from openai import OpenAI

# Load API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# App title and intro
st.set_page_config(page_title="Mindful English", page_icon="🧘‍♀️")
st.title("🧘‍♀️ Mindful English")
st.write("Practice English while reflecting mindfully. Get kind, constructive feedback from an AI language coach.")

# Prompt options
prompt = st.selectbox(
    "Choose a reflection prompt:",
    [
        "What was the best part of your day?",
        "What helps you feel calm?",
        "What do you appreciate about yourself?",
        "Describe something beautiful you saw recently.",
    ]
)

# Text input
user_input = st.text_area("Write a short response in English:")

# Button to trigger AI feedback
if st.button("Get gentle feedback") and user_input:
    with st.spinner("Thinking kind thoughts..."):
        # System message to instruct the assistant
        system_msg = (
            "You are a kind English tutor and mindfulness coach. "
            "When the user writes, gently correct or paraphrase their text in natural English. "
            "Offer an affirming message to support their confidence."
        )

        # Call the OpenAI Chat Completion API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if your key has access
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": f"Prompt: {prompt}\nUser text: {user_input}"}
            ],
            temperature=0.7
        )

        # Extract the response content
        feedback = response.choices[0].message.content

        # Show the result
        st.success("Here’s your reflection:")
        st.markdown(feedback)
