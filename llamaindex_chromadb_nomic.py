# Defining chromaDB

import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext

db = chromadb.PersistentClient(path="./nomicEmbed_db_llamaindex")
chroma_collection = db.get_or_create_collection("testing")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Define Embeddings
from llama_index.embeddings.ollama import OllamaEmbedding

ollama_embedding = OllamaEmbedding(model_name="nomic-embed-text")

# Data Loading
from llama_index.core import SimpleDirectoryReader

filename = r"sample.pdf"
documents = SimpleDirectoryReader(input_files=[filename]).load_data()

# Data Ingestion
from llama_index.core import VectorStoreIndex

index = VectorStoreIndex.from_documents(documents, storage_context=storage_context, embed_model=ollama_embedding)