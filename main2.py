import streamlit as st
import google.generativeai as genai

# Safely load API key
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("GOOGLE_API_KEY is missing in Streamlit secrets. Please add it under 'Manage App → Secrets'.")
    st.stop()

# Initialize Google Generative AI client
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Streamlit page setup
st.set_page_config(page_title="YouTube Evaluation Generator", layout="wide")
st.title("YouTube Evaluation Generator")

st.markdown(
    "Enter the YouTube ad video details below and click **Generate** to receive a full creative and strategic evaluation."
)

# Input fields
video_title = st.text_input("Enter YouTube Video Title")
video_description = st.text_area("Enter YouTube Video Description", height=200)

if st.button("Generate Evaluation"):
    if not video_title or not video_description:
        st.warning("Please provide both a video title and description before generating.")
    else:
        progress = st.progress(0, text="Starting evaluation...")

        prompt = f"""
             You are an expert marketing analyst for AMICA Insurance. Please provide a factual and specific creative and strategic evaluation of the following AMICA YouTube ad video based ONLY on the information provided in the title and description.

        Video Title: {video_title}

        Video Description: {video_description}

        IMPORTANT: This is specifically an AMICA insurance advertisement. Do not reference or compare to other insurance companies unless they are explicitly mentioned in the video description.

        Your output should include:

            1. Runtime & Format Overview:
            
            Based on the description, note what you can about the length and format.
            Only mention specific technical details like HD/4K if mentioned in the description.
            
            2. Scene-by-Scene Breakdown:
            
            Based strictly on what's described in the video description, break down what appears to be happening.
            Avoid making up scenes or details not mentioned in the description.
            
            3. Visual & Brand Identity:
            
            Discuss AMICA's brand identity elements mentioned in the description.
            Only mention colors, logos, and branding elements explicitly described.
            
            4. Emotional and Strategic Narrative:
            
            Analyze how AMICA is positioning itself emotionally and strategically.
            Focus on the specific message being conveyed about AMICA's insurance offerings.
            
            5. Competitive Positioning:
            
            Only compare to competitors if specifically mentioned in the description.
            If no competitors are mentioned, focus on how AMICA positions itself in the insurance market.
            
            6. Final Evaluation Scorecard:
            
            Create a scorecard evaluating different aspects of the AMICA ad.
            Be factual and avoid speculation about elements not described.
            
            7. Key Takeaways and Opportunities:
            
            Discuss the strengths of the AMICA ad based on the description.
            Suggest realistic improvements relevant to AMICA's brand and messaging.

        Present the output in structured bullet points and tables where appropriate.
        """

        try:
            progress.progress(25, text="Sending request to Google Gemini...")
            
            model = genai.GenerativeModel('gemini-1.5-pro')  # This is the correct identifier for Gemini 2.5 Pro
            
            # Generate content with higher temperature for more creative responses
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.5,  # Increased temperature for more creative responses
                    max_output_tokens=2048
                )
            )
            
            # Generate content
            response = model.generate_content(prompt)
            
            progress.progress(75, text="Processing response...")

            # Extract the generated text from the response
            evaluation = response.text

            progress.progress(100, text="Completed.")
            st.subheader("Generated Evaluation")
            st.markdown(evaluation)

            st.download_button(
                label="Download Evaluation as Text",
                data=evaluation,
                file_name="youtube_evaluation.txt",
                mime="text/plain"
            )

        except Exception as e:
            progress.empty()
            st.error("An error occurred during the Google Gemini request.")
            st.exception(e)

st.sidebar.markdown(
    "Provide the video title and description, then click Generate. The app will use Google's Gemini 2.5 Pro to produce a detailed evaluation."
)
