import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# CSS Style Background
st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background-color: #f7f8fc;
    }

    /* Main text */
    h1, h2, h3, h4, p, div, label {
        color: #1f2937;
    }

    /* Tabs (neutral grey style) */
    .stTabs [data-baseweb="tab"] {
        background-color: #eef1f6;
        color: #1f2937;
        border-radius: 8px 8px 0px 0px;
        padding: 8px 14px;
        border: 1px solid #d6dbe6;
    }

    /* Active tab (subtle blue, not purple) */
    .stTabs [aria-selected="true"] {
        background-color: #dbeafe;
        color: #1e3a8a;
        border-bottom: 2px solid #3b82f6;
    }

    /* Clean container spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

## Main Dashboard Code

#st.image(r'C:\Users\welcome\Desktop\BSMS1306\streamlit\Header.png')
st.image('Header.jpg')

#st.date_input("Select a date")

st.title("""Dashboard for Teen Media Habits and Mental Health
### Objective of Analysis\nTo analyze the factors that influence teenage mental health and identify how social media usage, sleep habits, physical activity, and social interactions are associated with mental health risk among teenagers.""")
    
#upload data
#upload_file = st.file_uploader("Please upload here:", type = 'csv')
    
  
#df = pd.read_csv(r"C:\Users\welcome\Desktop\BSMS1306\streamlit\Tips.csv")
df = pd.read_csv("clean_data.csv")
#df = pd.read_csv(upload_file)

tab1, tab2, tab3, tab4 = st.tabs(["Raw Data", "Histogram", "Scatter Chart", "Bar Chart"])


with tab1:
    #show data
    st.subheader("Raw Data")
    st.write(df)

#Histogram
with tab2:
    st.subheader("Histogram")
    numeric_columns = df.select_dtypes(include='number').columns
    column = st.selectbox("Choose a column", numeric_columns)
    fig, ax = plt.subplots(figsize = (10,6))
    df[column].plot(
    kind='hist',
    ax=ax,
    edgecolor='black', 
    linewidth=1.2,     
    color='steelblue'   
    )
    st.pyplot(fig)
    #fig = px.histogram(df, x=column)
    #fig.update_traces( marker = {"color":"purple", "line":{"color":"black","width":2}})
    #st.plotly_chart(fig)

#Scatter chart
with tab3:
    st.subheader("Scatter Chart")
    numeric_columns = df.select_dtypes(include='number').columns
    x_column = st.selectbox("Choose x-axis column", numeric_columns)
    y_column = st.selectbox("Choose y-axis column", numeric_columns)
    fig, ax = plt.subplots(figsize = (10,6))
    df.plot(kind = 'scatter', x=x_column, y=y_column, ax =ax)
    st.pyplot(fig)

    #fig = px.scatter(df, x=x_column, y = y_column,color ='sex' , color_discrete_sequence= ['yellow', 'red'])
    #st.plotly_chart(fig)

#Bar chart
with tab4:
    st.subheader("Bar Chart")
    categorical_columns = df.select_dtypes(include='object').columns
    column = st.selectbox("Choose a column", categorical_columns)
    fig, ax = plt.subplots(figsize=(10,6))
    df[column].value_counts().plot(
        kind='bar',
        ax=ax,
        color='steelblue',
        edgecolor='black', 
        linewidth=1.2  
    )
    st.pyplot(fig)

st.subheader("Discussion")
st.write("The analysis shows that social media usage, sleep patterns, physical activity, and social interaction are linked to teenagers’ mental health. Higher social media use and poor sleep are generally associated with higher stress, anxiety, and mental health risk, while healthier habits show better outcomes.")

st.subheader("Conclusion")
st.write("This project shows that lifestyle and digital habits are related to teenage mental health. Better sleep, regular exercise, and controlled social media use are associated with improved well-being. The results show patterns but not causation.")
