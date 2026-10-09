import faiss

index = faiss.read_index("documents.index")
print("Vectors loaded:", index.ntotal)

# 8AM (IST) LLM'S