import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommendation System", page_icon=":tv:", layout="wide")
load_dotenv()

@st.cache_resource 
def init_pipeline():
    return AnimeRecommendationPipeline()
pipeline = init_pipeline()

st.title("Anime Recommendation System")

query = st.text_input("Enter your anime preferences eg.: 'I want to watch an anime with action and adventure genre'")
if query:
    with st.spinner("Generating recommendations..."):
        recommendations = pipeline.recommend(query)
        st.success("Recommendations generated successfully")
        st.markdown("### Recommendations")
        st.write(recommendations)