from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, vector_store_path="chroma_db"):
        try:
            logger.info("Initializing Anime Recommendation Pipeline")

            vector_builder = VectorStoreBuilder(csv_path="", vector_store_path=vector_store_path)

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)
            logger.info("Anime Recommendation Pipeline initialized successfully")
        
        except Exception as e:
            logger.error(f"Error initializing Anime Recommendation Pipeline: {str(e)}")
            raise CustomException("Error initializing Anime Recommendation Pipeline", e)

    def recommend(self, query:str):
        try:
            logger.info(f"Recommendation query: {query}")
            return self.recommender.get_recommendations(query)
        except Exception as e:
            logger.error(f"Error getting recommendations: {str(e)}")
            raise CustomException("Error getting recommendations", e)

        