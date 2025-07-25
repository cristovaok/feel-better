import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]  # Store this safely in secrets

st.title("🧘‍♀️ Mindful English")
st.write("Practice English and mindfulness in one gentle space.")

prompt = st.selectbox(
    "Choose a reflection prompt:",
    [
        "What was the best part of your day?",
        "What helps you feel calm?",
        "What do you appreciate about yourself?",
        "Describe something beautiful you saw recently.",
    ]
)

user_input = st.text_area("Write a short answer in English:")

if st.button("Get gentle feedback") and user_input:
    with st.spinner("Thinking kind thoughts..."):
        system_msg = (
            "You are a kind English tutor and mindfulness coach. "
            "When the user writes, gently correct or paraphrase their text. "
            "Encourage them with a soft, affirming message too."
        )

        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": f"Prompt: {prompt}\nUser text: {user_input}"}
            ],
            temperature=0.7
        )

        feedback = response['choices'][0]['message']['content']
        st.success("Here’s your reflection:")
        st.markdown(feedback)
