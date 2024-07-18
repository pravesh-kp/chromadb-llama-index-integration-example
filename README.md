# chromadb-llama-index-integration-example
Introduction:
      The chromadb-llama-index-integration repository shows how to use ChromaDB and LlamaIndex together to store and process documents efficiently. It includes examples and instructions to help you get started. You can use this to build advanced applications like knowledge management systems and content recommendation engines.

Points to Note:
    1.The code sets up a ChromaDB-based vector store.
    2.It defines an embedding model using the OllamaEmbedding class.
    3.It loads a PDF document using the SimpleDirectoryReader class.
    4.It creates a vector store-based index using the VectorStoreIndex class.

The required pip installations are:
      chromadb
      llama-index
      ollama-embedding
      
The code demonstrates the integration of ChromaDB and LlamaIndex for document processing and storage. Here’s a breakdown of the key steps:
  1.Setting up ChromaDB: 
          The code creates a persistent ChromaDB client and specifies the path where the database will be stored. It then creates a new ChromaDB collection named "testing" or retrieves an existing one.
  2.Defining Embeddings: 
          The code imports the OllamaEmbedding class from the LlamaIndex library and creates an instance of it using the "nomic-embed-text" model.
Loading Data: The code loads data from a PDF file using the SimpleDirectoryReader class. It specifies the filename of the PDF document and loads the data into a list of documents.
  3.Ingesting Data: 
          The code creates a VectorStoreIndex instance using the loaded documents, the StorageContext instance, and the OllamaEmbedding instance as input. This process ingests the documents into the vector store.

