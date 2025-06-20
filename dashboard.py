import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/ds_salaries.csv')

st.title('LinkedIn Job Posting Analysis Dashboard')

st.markdown('## Summary Metrics')

col1, col2, col3 = st.columns(3)
col1.metric(label="Total Job Postings", value=len(df))
col2.metric(label="Unique Job Titles", value=df['Job Title'].nunique())
col3.metric(label="Unique Locations", value=df['Location'].nunique())

st.markdown('---')


st.sidebar.header('Filters')

selected_locations = st.sidebar.multiselect('Select Location(s):', options=df['Location'].unique())

if selected_locations:
    filtered_df = df[df['Location'].isin(selected_locations)]
else:
    filtered_df = df

st.subheader('Top In-Demand Job Titles')
job_counts = filtered_df['Job Title'].value_counts().head(10)
st.bar_chart(job_counts)

st.markdown('---')

st.subheader('Top Hiring Locations')
location_counts = filtered_df['Location'].value_counts().head(10)
st.bar_chart(location_counts)

st.markdown('---')

st.subheader('Most In-Demand Skills')

skills = ['Python', 'SQL', 'Excel', 'Tableau', 'Machine Learning', 'R', 'Power BI', 'Hadoop', 'Spark', 'AWS']

if 'Job Description' in filtered_df.columns:
    for skill in skills:
        filtered_df[skill] = filtered_df['Job Description'].str.lower().apply(lambda x: 1 if skill.lower() in x else 0)

    skill_counts = filtered_df[skills].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=skill_counts.values, y=skill_counts.index, palette='plasma', ax=ax)
    ax.set_xlabel('Number of Job Postings')
    ax.set_ylabel('Skill')
    ax.set_title('Top In-Demand Skills')

    st.pyplot(fig)
else:
    st.error("The column 'Job Description' is missing from the dataset.")
