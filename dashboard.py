import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="LinkedIn Job Analysis Dashboard", page_icon="📊", layout="wide")


with st.spinner('Loading data...'):
    df = pd.read_csv('data/ds_salaries.csv')

st.success('Data Loaded Successfully! ✅')


st.title('LinkedIn Job Posting Analysis Dashboard')


st.markdown('## Summary Metrics')

col1, col2, col3 = st.columns(3)
col1.metric(label="💼 Total Job Postings", value=len(df))
col2.metric(label="📌 Unique Job Titles", value=df['Job Title'].nunique())
col3.metric(label="🌍 Unique Locations", value=df['Location'].nunique())

st.markdown('---')


st.sidebar.header('Filters')
selected_locations = st.sidebar.multiselect('Select Location(s):', options=df['Location'].unique())

if selected_locations:
    filtered_df = df[df['Location'].isin(selected_locations)]
else:
    filtered_df = df


st.subheader('Top In-Demand Job Titles')
job_counts = filtered_df['Job Title'].value_counts().head(10).reset_index()
job_counts.columns = ['Job Title', 'Count']

fig_job = px.bar(job_counts, x='Job Title', y='Count', color='Count',
                 title='Top In-Demand Job Titles', hover_data={'Count': True},
                 color_continuous_scale='blues')
fig_job.update_layout(xaxis_title=None, yaxis_title='Number of Job Postings')

st.plotly_chart(fig_job)

st.markdown('---')


st.subheader('Top Hiring Locations')
location_counts = filtered_df['Location'].value_counts().head(10).reset_index()
location_counts.columns = ['Location', 'Count']

fig_loc = px.bar(location_counts, x='Location', y='Count', color='Count',
                 title='Top Hiring Locations', hover_data={'Count': True},
                 color_continuous_scale='blues')
fig_loc.update_layout(xaxis_title=None, yaxis_title='Number of Job Postings')

st.plotly_chart(fig_loc)

st.markdown('---')


st.subheader('Most In-Demand Skills')

skills = ['Python', 'SQL', 'Excel', 'Tableau', 'Machine Learning', 'R', 'Power BI', 'Hadoop', 'Spark', 'AWS']

if 'Job Description' in filtered_df.columns:
    for skill in skills:
        filtered_df[skill] = filtered_df['Job Description'].str.lower().apply(lambda x: 1 if skill.lower() in x else 0)

    skill_counts = filtered_df[skills].sum().sort_values(ascending=False).reset_index()
    skill_counts.columns = ['Skill', 'Count']

    fig_skill = px.bar(skill_counts, x='Count', y='Skill', orientation='h', color='Count',
                       title='Top In-Demand Skills', hover_data={'Count': True},
                       color_continuous_scale='blues')
    fig_skill.update_layout(xaxis_title='Number of Job Postings', yaxis_title=None)

    st.plotly_chart(fig_skill)
else:
    st.error("The column 'Job Description' is missing from the dataset.")


st.markdown("""
---
<p style='text-align: center;'>Created by Garv Agarwal | © 2025 LinkedIn Job Analysis</p>
""", unsafe_allow_html=True)
