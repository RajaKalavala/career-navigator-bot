import streamlit as st
import pandas as pd
import openai
import json

# Load the dataset
career_data = pd.read_csv("career_dataset.csv")

# OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Helper: Find matching careers
def find_matching_careers(interests, skills):
    keywords = set(map(str.strip, (interests + ',' + skills).lower().split(',')))
    matches = []

    for _, row in career_data.iterrows():
        score = 0
        if not isinstance(row['required_skills'], str): continue
        skill_text = row['required_skills'].lower()
        title_text = row['career_name'].lower()
        for keyword in keywords:
            if keyword in skill_text or keyword in title_text:
                score += 1
        if score > 0:
            matches.append((row['career_name'], score))
    
    return sorted(matches, key=lambda x: x[1], reverse=True)[:3]

# Helper: Get full career info
def get_career_details(career_name):
    row = career_data[career_data['career_name'].str.lower() == career_name.lower()]
    if row.empty:
        return None
    row = row.iloc[0]
    return {
        "Career Name": row['career_name'],
        "Required Skills": row['required_skills'],
        "Learning Path": row['learning_path'],
        "Common Job Titles": row['common_job_titles'],
        "Recommended Tools": row['recommended_tools']
    }

# Streamlit UI
st.title("Career Navigator Bot")

with st.form("career_form"):
    interests = st.text_input("What are your interests?")
    skills = st.text_input("What skills do you have?")
    submitted = st.form_submit_button("Find Career Paths")

if submitted:
    st.subheader("Top Career Matches")
    matches = find_matching_careers(interests, skills)

    if matches:
        career_names = [c[0] for c in matches]
        selected_career = st.selectbox("Select a career to explore further:", career_names)

        if selected_career:
            info = get_career_details(selected_career)
            st.success("Here is your personalized career guidance:")
            st.write(f"**Career Name:** {info['Career Name']}")
            st.write(f"**Required Skills:** {info['Required Skills']}")
            st.write(f"**Learning Path:** {info['Learning Path']}")
            st.write(f"**Common Job Titles:** {info['Common Job Titles']}")
            st.write(f"**Recommended Tools:** {info['Recommended Tools']}")
    else:
        st.warning("No matching careers found. Try different inputs.")
