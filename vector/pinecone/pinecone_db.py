
import os
from dotenv import load_dotenv
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

load_dotenv()

# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Connect to Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("python-learning")

# 3. Sample documents
documents = [
    {
        "id": "doc1",
        "text": "Python is a programming language.",
        "category": "Python"
    },
    {
        "id": "doc2",
        "text": "Machine learning helps computers learn from data.",
        "category": "AI"
    },
    {
        "id": "doc3",
        "text": "React is used to build user interfaces.",
        "category": "Web Development"
    }
]

# 4. Create embeddings and store them
vectors = []

#5. Each text converted to embedding with the help of sentence-transformers model 

for doc in documents:
    embedding = model.encode(doc["text"]).tolist()

    vectors.append({
        "id": doc["id"],
        "values": embedding,
        "metadata": {
            "text": doc["text"],
            "category": doc["category"]
        }
    })
#6. stored in the database using upsert method.
#why upsert method is inserting the embeddings into the database. 
# It will insert the embeddings if they do not exist, or update them if they already exist.

index.upsert(vectors=vectors)
print("Documents stored successfully!")

# 5. Search by meaning
question = input("Enter your question: ")

query_embedding = model.encode(question).tolist()

results = index.query(
    vector=query_embedding,
    top_k=2,
    include_metadata=True
)

# 6. Display results
print("\nMost relevant documents:")

for match in results.matches:
    print("ID:", match.id)
    print("Score:", round(match.score, 4))
    print("Text:", match.metadata["text"])
    print("Category:", match.metadata["category"])
    print("-" * 40)