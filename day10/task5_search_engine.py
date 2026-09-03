import numpy as np


# --------------------------------------------------
# 1. Vocabulary
# --------------------------------------------------

vocab = ['ml', 'data', 'model', 'cook', 'recipe', 'food']


# --------------------------------------------------
# 2. Documents
# --------------------------------------------------

docs = np.array([
    [8, 6, 4, 0, 0, 1],   # Document 1 - ML
    [0, 1, 0, 7, 8, 6],   # Document 2 - Cooking
    [9, 7, 5, 0, 0, 0],   # Document 3 - ML, same topic as query
    [8, 6, 4, 0, 0, 0],   # Document 4 - ML, similar to query
    [40, 30, 20, 0, 0, 0]  # Document 5 - ML, 5x Document 4
])


# --------------------------------------------------
# 3. Query
# --------------------------------------------------

query = np.array([9, 7, 5, 0, 0, 0])


# --------------------------------------------------
# 4. Cosine similarity function
# --------------------------------------------------

def cosine_similarity(a, b):
    numerator = np.dot(a, b)

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0

    return numerator / denominator


# --------------------------------------------------
# 5. Calculate cosine similarity
# --------------------------------------------------

cosine_scores = []

for i, doc in enumerate(docs):
    score = cosine_similarity(query, doc)
    cosine_scores.append((i + 1, score))


# Sort from highest to lowest
cosine_scores.sort(key=lambda x: x[1], reverse=True)


# --------------------------------------------------
# 6. Display cosine ranking
# --------------------------------------------------

print("=" * 50)
print("RANKING BY COSINE SIMILARITY")
print("=" * 50)

for rank, (doc_number, score) in enumerate(cosine_scores, start=1):
    print(
        f"Rank {rank}: Document {doc_number} "
        f"-> cosine similarity = {score:.4f}"
    )


# --------------------------------------------------
# 7. Rank using raw dot product
# --------------------------------------------------

dot_scores = []

for i, doc in enumerate(docs):
    score = np.dot(query, doc)
    dot_scores.append((i + 1, score))


# Sort from highest to lowest
dot_scores.sort(key=lambda x: x[1], reverse=True)


# --------------------------------------------------
# 8. Display dot-product ranking
# --------------------------------------------------

print("\n" + "=" * 50)
print("RANKING BY RAW DOT PRODUCT")
print("=" * 50)

for rank, (doc_number, score) in enumerate(dot_scores, start=1):
    print(
        f"Rank {rank}: Document {doc_number} "
        f"-> dot product = {score}"
    )


# --------------------------------------------------
# 9. Self-similarity
# --------------------------------------------------

self_similarity = cosine_similarity(query, query)

print("\n" + "=" * 50)
print("SELF SIMILARITY")
print("=" * 50)

print(f"Cosine(query, query) = {self_similarity:.4f}")


# --------------------------------------------------
# 10. Length experiment
# --------------------------------------------------

print("\n" + "=" * 50)
print("LENGTH EXPERIMENT")
print("=" * 50)

doc_4 = docs[3]
doc_5 = docs[4]

print("Document 4:", doc_4)
print("Document 5:", doc_5)

print(
    f"Cosine similarity = "
    f"{cosine_similarity(doc_4, doc_5):.4f}"
)

print(
    f"Dot product = "
    f"{np.dot(doc_4, doc_5)}"
)




#Cosine similarity is useful for comparing documents because it measures the angle between their vectors rather than being strongly affected by document length. Therefore, two documents with similar word patterns can receive similar scores even when one is much longer than the other.