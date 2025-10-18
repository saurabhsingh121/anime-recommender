from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

class VectorStoreBuilder:
    def __init__(self, csv_path: str, vector_store_path: str="./chroma_db"):
        self.csv_path = csv_path
        self.vector_store_path = vector_store_path
        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    
    def build_and_save_vector_store(self):
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding="utf-8",
            metadata_columns=[]
            )
        
        data = loader.load()

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = splitter.split_documents(data)

        db = Chroma.from_documents(texts, embedding=self.embedding, persist_directory=self.vector_store_path)
        db.persist()

    
    def load_vector_store(self):
        return Chroma(persist_directory=self.vector_store_path, embedding_function=self.embedding)
