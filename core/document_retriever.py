from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class DocumentRetriever:
    def __init__(self, text: str, chunk_size=500, similarity_threshold: float = 0.2):
        self.text = text
        self.chunks = self.chunk_text(chunk_size)
        self.vectorizer = TfidfVectorizer()
        self.similarity_threshold = similarity_threshold

    def chunk_text(self, chunk_size):
        chunks = []
        for i in range(0, len(self.text), chunk_size):
            chunks.append(self.text[i:i + chunk_size])
        return chunks

    def retrieve(self, query: str) -> list:
        if not query:
            return ["No query provided."]

        chunk_vectors = self.vectorizer.fit_transform(self.chunks)
        query_vector = self.vectorizer.transform([query])

        similarity_scores = cosine_similarity(query_vector, chunk_vectors).flatten()
        relevant_chunks = sorted(zip(similarity_scores, self.chunks), reverse=True, key=lambda x: x[0])[:3]
        relevant_docs = [chunk for score, chunk in relevant_chunks if score >= self.similarity_threshold]

        if relevant_docs:
            return relevant_docs
        else:
            return ["Sorry, I don't have information related to your query."]
