# import chromadb
import chromadb

# import SentenceTransformer
from sentence_transformers import SentenceTransformer

# import model
# this model used to create embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# define the db location
client = chromadb.PersistentClient(
    path="./chroma_db"
)

# table & database - programming
collection = client.get_or_create_collection(name="programming")

print("DataBase and Collection Created !!!")

# documents & ids 
documents=["Python is a programming language",            
             "Java is used for software development",
             "I love machine learning",
             "Deep learning uses neural networks",
             "Python is eazy to learn"]

ids=["1","2","3","4","5"]

# create embeddings for the documents.
#encode the documents to create embeddings.
#tolist() is used to convert the numpy array to list.
embeddings = model.encode(documents).tolist()

# These documents, ids converted to embeddings with the help of sentence-transformers model and 
# stored in the database using upsert method.
collection.upsert(
    ids=ids,
    documents=documents,
    embeddings=embeddings
)
#Know the number of documents stored in the database.
print(collection.count())


#Similarity search - query the database to find similar documents based on a query.
query = "what is python ?"

# Can we convert the query to embedding using the same model and 
# then use the query_embedding to find similar documents in the database.
# we need to convert this list using tolist() method.

query_embedding = model.encode(query).tolist()

#Similarity search - query the database to find similar documents based on a query.
#query_embeddings is used to find the similar documents in the database.
#we need top_results to get the top 2 similar documents from the database.
res = collection.query(
    query_embeddings = [query_embedding],
    n_results = 2
)
print(res)

