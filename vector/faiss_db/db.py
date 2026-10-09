from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# loading embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = ["Python is a programming language",            
             "Java is used for software development",
             "I love machine learning",
             "Deep learning uses neural networks",
             "Python is eazy to learn",
             "Java is a popular programming language",  ]

# create embeddings
embeddings = model.encode(documents)

# convert embedding to float
embeddings = np.array(embeddings,dtype="float32")
dimension = embeddings.shape[1]

# create faiss db (with 384)
index = faiss.IndexFlatL2(dimension)

# add records to faiss
index.add(embeddings)

# print records from faiss db
print(index.ntotal)

# Similarity Search
query = ["I want to learn Python"]
query_embeddings = model.encode(query)
query_embeddings = np.array(query_embeddings,dtype="float32")
distances,indexes = index.search(query_embeddings, 2)

print(indexes, distances)

# Example 4: Insert more documents

new_documents = [
    "React is a JavaScript library",
    "FastAPI is a Python web framework"
]

# Convert new documents into embeddings
new_embeddings = model.encode(new_documents)

new_embeddings = np.array(
    new_embeddings,
    dtype="float32"
)

# Insert into existing FAISS index
index.add(new_embeddings)

# Add documents to our document list
documents.extend(new_documents)

print("Total vectors:", index.ntotal)
print("Total documents:", len(documents))

#Example 5: Search for similar documents after adding new documents
query = ["I want to develop a frontend application"]

query_embedding = model.encode(query)
query_embedding = np.array(
    query_embedding,
    dtype="float32"
)

distances, indexes = index.search(query_embedding, 3)

for i, doc_id in enumerate(indexes[0]):
    print("Document:", documents[doc_id])
    print("Distance:", distances[0][i])
    print("----------------")

    # Update document at position 0
documents[0] = "Python is widely used in AI development"

# Generate embeddings for all updated documents
embeddings = model.encode(documents)
embeddings = np.array(embeddings, dtype="float32")

# Rebuild the index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

print("Updated index count:", index.ntotal)
print("Updated document:", documents[0])

faiss.write_index(index, "documents.index")
print("Index saved")