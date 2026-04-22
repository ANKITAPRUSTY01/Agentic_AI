from sentence_transformers import SentenceTransformer
import chromadb

# load model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# KB
docs = [
    "Python is a programming language widely used in AI and Machine Learning.",
    "Machine Learning is a method where systems learn patterns from data.",
    "Deep Learning is a subset of Machine Learning using neural networks.",
    "SQL is used to manage and query relational databases.",
    "Data Science combines statistics, programming, and domain knowledge.",
    "Natural Language Processing helps machines understand human language.",
    "AI Engineers build intelligent systems using ML and DL.",
    "To become an AI Engineer, learn Python, Machine Learning, Deep Learning, and NLP.",
    "TensorFlow and PyTorch are popular Deep Learning frameworks.",
    "Scikit-learn is used for Machine Learning tasks."
]

texts = docs
embeddings = embedder.encode(texts).tolist()

ids = [f"doc_{i}" for i in range(len(texts))]
metadatas = [{"source": f"doc_{i}"} for i in range(len(texts))]

client = chromadb.Client()
collection = client.create_collection(name="career_ai")

collection.add(
    documents=texts,
    embeddings=embeddings,
    ids=ids,
    metadatas=metadatas
)

print("ChromaDB Ready ✅")