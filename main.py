import streamlit as st
from openai import OpenAI

# Streamlit page setup
st.set_page_config(page_title="YouTube Evaluation Generator", layout="wide")
st.title("🎥 YouTube Evaluation Generator")

# Safely load API key
st.write("🔍 Checking for OpenAI API key...")
if "OPENAI_API_KEY" not in st.secrets:
    st.error("❌ OPENAI_API_KEY is missing in Streamlit secrets. Please add it under 'Manage App → Secrets'.")
    st.stop()
else:
    st.success("✅ Found OpenAI API key.")

# Initialize OpenAI client
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    st.write("✅ OpenAI client initialized successfully.")
except Exception as e:
    st.exception(f"❌ Failed to initialize OpenAI client: {e}")
    st.stop()

st.markdown(
    "Enter the YouTube ad video details below and click **Generate** to receive a full creative and strategic evaluation."
)

# Input fields
video_title = st.text_input("Enter YouTube Video Title")
video_description = st.text_area("Enter YouTube Video Description", height=200)

if st.button("Generate Evaluation"):
    if not video_title or not video_description:
        st.warning("⚠️ Please provide both a video title and description before generating.")
    else:
        st.write("🔄 Preparing prompt...")
        prompt = f"""
        You are an expert marketing analyst. Please provide a full creative and strategic evaluation of the following YouTube ad video.

        Video Title: {video_title}

        Video Description: {video_description}

        Your output should include:
        1. Runtime & Format Overview
        2. Scene-by-Scene Breakdown
        3. Visual & Brand Identity
        4. Emotional and Strategic Narrative
        5. Competitive Positioning (compared to GEICO, State Farm, Progressive, Allstate)
        6. Final Evaluation Scorecard
        7. Key Takeaways and Opportunities

        Present the output in structured bullet points and tables where appropriate.
        """

        with st.spinner("⏳ Generating evaluation... please wait."):
            try:
                st.write("🚀 Sending request to OpenAI...")
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.5
                )
                st.success("✅ Response received from OpenAI.")

                evaluation = response.choices[0].message.content
                st.subheader("📊 Generated Evaluation")
                st.markdown(evaluation)

                st.download_button(
                    label="📥 Download Evaluation as Text",
                    data=evaluation,
                    file_name="youtube_evaluation.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error("❌ An error occurred during the OpenAI request.")
                st.exception(e)
