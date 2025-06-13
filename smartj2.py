import streamlit as st
import pandas as pd

st.set_page_config(
    page_title=" MatchAble",
    layout="centered"
)

@st.cache_data
def load_data():
    try:
        jobs = pd.read_csv("jobs.csv")
        candidates = pd.read_csv("candidates.csv")
        if 'Salary' in jobs.columns:
            jobs['Salary'] = jobs['Salary'].str.replace('$', '').str.replace(',', '').astype(float)
        return jobs, candidates
    except Exception as e:
        st.error(f"Error loading CSV files: {e}")
        return pd.DataFrame(), pd.DataFrame()

jobs_df, candidates_df = load_data()

st.title("♿ MatchAble Job Matcher")
st.write("Matching disabled workers with suitable jobs from your datasets")

st.sidebar.title("Filters")
selected_candidate = st.sidebar.selectbox(
    "Select a candidate:",
    candidates_df['Name'].unique(),
    index=0
)
work_type_options = ["All"] + list(jobs_df['Accessibility'].unique())
selected_work_type = st.sidebar.selectbox(
    "Work Type:",
    work_type_options,
    index=0
)
location_options = ["All"] + list(jobs_df['Location'].unique())
selected_location = st.sidebar.selectbox(
    "Location:",
    location_options,
    index=0
)

def find_matches(candidate, jobs_df, work_type="All", location="All"):
    candidate_skills = [s.strip().lower() for s in candidate['Skills'].split(',')]
    candidate_needs = [n.strip().lower() for n in candidate['Needs'].split(',')]
    filtered_jobs = jobs_df.copy()
    if work_type != "All":
        filtered_jobs = filtered_jobs[filtered_jobs['Accessibility'] == work_type]
    if location != "All":
        filtered_jobs = filtered_jobs[filtered_jobs['Location'] == location]
    def score_job(job):
        job_skills = [s.strip().lower() for s in job['Skills'].split(',')]
        job_access = str(job['Accessibility']).strip().lower()
        skill_match = len(set(candidate_skills) & set(job_skills))
        need_match = sum(need in job_access for need in candidate_needs)
        return skill_match + need_match
    filtered_jobs['MatchScore'] = filtered_jobs.apply(score_job, axis=1)
    return filtered_jobs[filtered_jobs['MatchScore'] > 0].sort_values(by='MatchScore', ascending=False)

candidate_row = candidates_df[candidates_df['Name'] == selected_candidate].iloc[0]
matches = find_matches(candidate_row, jobs_df, selected_work_type, selected_location)

st.header(f"Job Matches for {selected_candidate}")
if matches.empty:
    st.info("No matching jobs found. Try adjusting the filters.")
else:
    st.dataframe(matches[['Title', 'Location', 'Accessibility', 'Salary', 'MatchScore',]])