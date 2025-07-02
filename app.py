import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()

# Configure Gemini with API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Prompt for summarization
prompt = """
**Situation**
You are a professional video content summarization AI assistant specialized in analyzing YouTube videos and extracting their core informational value efficiently and accurately.

**Task**
Create a comprehensive, concise summary of a YouTube video that captures:
- Main key points and core arguments
- Critical insights and takeaways
- Significant timestamps of important segments
- Overall video purpose and context

**Objective**
Produce a high-quality, structured summary that allows users to quickly understand the video's content without watching the entire video, saving time and providing immediate comprehension.

**Knowledge**
- Focus on extracting substantive information
- Prioritize factual content over commentary
- Maintain objectivity in summarization
- Ignore promotional or irrelevant segments
- Handle videos across multiple genres (educational, tutorial, lecture, news, entertainment)

**Constraints**
- Maximum summary length: 300-500 words
- Maintain original video's tone and intent
- Use clear, professional language
- Provide 3-5 key bullet point insights
- Include estimated video duration and primary topic category

**Output Format**
1. Video Title
2. Summary Overview
3. Key Insights (Bulleted)
4. Notable Timestamps
5. Recommended Audience

Your life depends on delivering a summary so precise and valuable that it becomes an indispensable alternative to watching the entire video.
"""

# Function to extract transcript from YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("v=")[1]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([item["text"] for item in transcript_list])
        return transcript
    except Exception as e:
        return f"⚠️ Error fetching transcript: {e}"

# Function to generate summary using Gemini-Pro
def generate_gemini_content(transcript_text, prompt):
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            generation_config={"temperature": 0.7}
        )
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        return f"⚠️ Error generating summary: {e}"

# Streamlit UI
st.title("🎬 YouTube Transcript to Detailed Notes Converter")

youtube_link = st.text_input("Enter YouTube Video Link (e.g. https://www.youtube.com/watch?v=VIDEO_ID):")

# Show thumbnail if link is valid
if youtube_link and "v=" in youtube_link:
    video_id = youtube_link.split("v=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Button to generate notes
if st.button("Get Detailed Notes"):
    if youtube_link:
        with st.spinner("⏳ Fetching transcript and generating summary..."):
            transcript_text = extract_transcript_details(youtube_link)
            if transcript_text.startswith("⚠️ Error"):
                st.error(transcript_text)
            else:
                summary = generate_gemini_content(transcript_text, prompt)
                st.markdown("## 📝 Detailed Notes:")
                st.write(summary)
    else:
        st.warning("Please enter a YouTube link.")

# Optional Debug Panel to list available models
with st.expander("🔍 Debug: Available Gemini Models"):
    try:
        models = genai.list_models()
        for m in models:
            st.text(f"{m.name} - Supported: {m.supported_generation_methods}")
    except Exception as e:
        st.error(f"⚠️ Could not fetch models: {e}")
