import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptAvailable
from openai import OpenAI
import re

# Load OpenAI API key
if "OPENAI_API_KEY" not in st.secrets:
    st.error("OPENAI_API_KEY is missing in Streamlit secrets. Please add it under 'Manage App → Secrets'.")
    st.stop()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit setup
st.set_page_config(page_title="YouTube Transcript Deep Evaluation", layout="wide")
st.title("YouTube Transcript Deep Evaluation")

st.markdown(
    "Enter a YouTube video URL. The app will fetch the transcript and generate a **careful, non-speculative GPT-4 evaluation** based strictly on the provided transcript."
)

def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else None

# Input
youtube_url = st.text_input("Enter YouTube Video URL")

if st.button("Fetch Transcript and Generate Evaluation"):
    video_id = extract_video_id(youtube_url)
    if not video_id:
        st.error("Could not extract video ID from the URL. Please check the link format.")
    else:
        progress = st.progress(0, text="Fetching transcript...")

        try:
            # Fetch transcript
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            transcript_text = " ".join([entry['text'] for entry in transcript_list])

            progress.progress(25, text="Transcript fetched. Preparing strict GPT-4 prompt...")

            prompt = f"""
            You are an expert marketing and media analyst. Your task is to carefully analyze the following YouTube ad video **using only the provided transcript**.
            
            You **must not** assume or invent any details not explicitly present in the transcript.
            Where information is missing (e.g., visuals, tone, music, editing), you should explicitly note the gap rather than speculate.

            Your evaluation should include:
            1. Overall Message and Theme — based only on spoken content.
            2. Scene-by-Scene Breakdown — strictly inferred from transcript.
            3. Emotional and Narrative Arc — only from spoken words.
            4. Brand Positioning and Audience Appeal — grounded in transcript content.
            5. Marketing Effectiveness — based solely on what is spoken.
            6. Recommendations — flag gaps where visual or audio context is missing and suggest what additional information would improve evaluation.
            7. Competitive Differentiation — cautiously, without assuming unknowns.

            Do not include imagined visuals, unknown settings, or non-transcript details.

            Provided Transcript:
            {transcript_text}
            """

            progress.progress(50, text="Sending request to GPT-4...")

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0  # lower temperature for factuality
            )

            progress.progress(90, text="Processing GPT-4 response...")

            evaluation = response.choices[0].message.content

            progress.progress(100, text="Completed.")
            st.subheader("Evaluation Results")
            st.markdown(evaluation)

            st.download_button(
                label="Download Evaluation as Text",
                data=evaluation,
                file_name="youtube_deep_evaluation.txt",
                mime="text/plain"
            )

        except TranscriptsDisabled:
            st.error("Transcripts are disabled for this video.")
        except NoTranscriptAvailable:
            st.error("No transcript available for this video.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

st.sidebar.markdown(
    "Provide the YouTube video URL and click the button. The app will strictly analyze the transcript without speculation or invented details."
)
