import streamlit as st
# make wide mode the default
st.set_page_config(layout="wide",initial_sidebar_state="expanded")

st.markdown("<h1 style='text-align: center;'>The Crystal Stockball: Fortune Telling for Investors</h1>", unsafe_allow_html=True)
st.divider()

# add a button called next: Project wlakthorugh that will take the user to the next page
left, middle, right = st.columns(3,gap='large')  
with left:
    st.page_link("Pages/Home.py",label = "About", icon = "📝")
    
with middle:
    st.page_link("Pages/Project.py",label = "Project walkthorugh", icon = "📚")  
    
with right:
    st.page_link("Pages/LiveModel.py",label = "Give the model a try!", icon = "🔮")
    
left, right = st.columns([2,1],gap='large')  
with left.container(border=True):     
    left.header("About this project", divider=True)

    left.markdown('''
        **This is an end-to-end data science project that aims to deploy an interactive model that will predict the stock price movement of a given stock ticker for the next day.**

        **This project will cover the following steps:**
        1. **Data collection** - We will collect historical stock price data from Yahoo Finance using the yfinance API.
        2. **Exploratory data analysis (EDA)** - We will explore the historical stock price data to understand the patterns and trends.
        3. **Feature engineering** - We will create new features from the historical stock price data to help predict the stock price movement.
        4. **Modeling** - We will train, optimize, and evaluate a variety of machine learning models.
        5. **Model deployment** - Finally, we will deploy the best performing model as a web application using Streamlit.            
        ''')

with right.container(border=True):     
    right.header("Skills & Tools Utilized",divider=True)
    # Skills dictionary with icons and descriptions
    skills = {
        "Github": {
            "icon": "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg"  # Github logo URL
        },
         "Machine Learning Frameworks": {
            "icon": "https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg"  # Scikit-learn logo URL
        },
        "Python": {
            
            "icon": "https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg" # Python logo URL
        },
        "Data Visualization": {
            "icon": "https://upload.wikimedia.org/wikipedia/commons/0/01/Created_with_Matplotlib-logo.svg" # Seaborn logo URL
        },
        "Streamlit": {
            "icon": "https://streamlit.io/images/brand/streamlit-mark-color.png"  # Streamlit logo URL
        },
        "Exploratory Data Analysis": {
            "icon": "https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" # Seaborn logo URL
        },
        "Generative AI": {
            "icon": "https://upload.wikimedia.org/wikipedia/commons/1/13/ChatGPT-Logo.png" # Chatpgt logo URL
        },
        "Model Selection, Evaluation, & Deployment": {
            "icon": "https://upload.wikimedia.org/wikipedia/commons/d/d9/LightGBM_logo_black_text.svg" # LGBM logo URL
        },
        "Feature Engineering": {
            "icon": "https://upload.wikimedia.org/wikipedia/commons/3/37/Yahoo_Finance_Logo_2019.png" # yahoo finance logo URL
        }
    }

        # Split the skills into groups of 4 for the layout
    skills_list = list(skills.items())
    for i in range(0, len(skills_list), 2):
        # Create 4 columns for each group of skills
        cols = right.columns(2)  # Create 4 columns
        for j in range(2):
            if i + j < len(skills_list):
                skill, details = skills_list[i + j]
                with cols[j]:
                        st.markdown(skill) # Skill name
                        
# add all logos on the same row
# Create a container for logos
st.divider()
logos = [details["icon"] for details in skills.values()]  # Extract logos from the skills dictionary

# Create columns for each logo
logo_cols = st.columns(len(logos))  # Create a column for each logo

# Populate the columns with logos
for index, logo in enumerate(logos):
    with logo_cols[index]:
        st.markdown(f'<img src="{logo}" style="height: 30px;">', unsafe_allow_html=True)


    # skills_list = list(skills.items())
    # num_columns = 2  # Total number of columns
    # rows_per_column = 4 # Number of rows for each column

    # # Create empty lists for logos and skill names
    # logos = [details["icon"] for _, details in skills_list]
    # skill_names = [skill for skill, _ in skills_list]

    # # Create columns
    # cols = right.columns(num_columns)

    # # Populate the grid
    # for i in range(rows_per_column):
    #     for col_index in range(num_columns):
    #         skill_index = i + (col_index * rows_per_column)
    #         if skill_index < len(skill_names):  # Ensure we don't go out of bounds
    #             with cols[col_index]:
    #                 st.image(logos[skill_index], width=40)  # Display skill icon
    #                 st.subheader(skill_names[skill_index])  # Skill name


