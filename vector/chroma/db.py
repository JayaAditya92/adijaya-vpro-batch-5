import chromadb

# define the location
client = chromadb.PersistentClient(
    path="./test_db"
)

# create the database/collection
collection = client.get_or_create_collection(name="courses")

print("DataBase and Collection Created !!!")

# insert the records
collection.add(
    ids=["1","2","3","4","5"],
    documents=["Python is a programming language",            
             "Java is used for software development",
             "I love machine learning",
             "Deep learning uses neural networks",
             "Python is easy to learn"]
)

print("5 documents are inserted !!!")

# fetch the data
results = collection.get()
print(results["ids"])
print(results["documents"])

# similarity search
result = collection.query(
    query_texts=["what is python"],
    n_results=2
)
print(result)

# update
collection.update(
    ids=["1"],
    documents = ["Python is widely used in machine learning and AI"]
)
print("Document Updated !!!")

# How to get the updated document
results = collection.get()
print(results["documents"])

#delete the document
collection.delete(ids=["2"])
print(collection.count())

#metadatas are used to store additional information about the documents. 
#Metadatas are tag/identity for the documents. 
# It can be used to filter the documents based on the metadata values as per dictionary key-value pair.
collection.add(
    ids=["2"],
    documents=["Agentic AI"],
    metadatas=[{"VPro":"VPro","Batch-5":"Batch-5"}]
)
print(collection.count())

#search the document based on the metadata value
#where is the keyword to filter the documents based on the metadata values as per dictionary key-value pair.
res1 = collection.get(
    where={"VPro":"VPro"}
)
print(res1)



