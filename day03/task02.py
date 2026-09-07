import string
from collections import Counter

# TASK 02 - WORD FREQUENCY WITH COUNTER

# STEP 1: Read the text file

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# STEP 2: Normalize the text

# Convert everything to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(
    str.maketrans("", "", string.punctuation)
)

# Split into words
words = text.split()

# STEP 3: Hard way
# Dictionary + loop + .get()

manual_counts = {}

for word in words:
    manual_counts[word] = manual_counts.get(word, 0) + 1

print("===== MANUAL COUNT =====")
print(manual_counts)

# STEP 4: Right way
# Counter

counter_counts = Counter(words)

print("\n===== COUNTER =====")
print(counter_counts)

# STEP 5: Compare top 10

print("\n===== TOP 10 WORDS =====")

top_10 = counter_counts.most_common(10)

for word, count in top_10:
    print(f"{word}: {count}")

# STEP 6: Stopwords

stopwords = {
    "the",
    "a",
    "an",
    "and",
    "is",
    "are",
    "of",
    "to",
    "in",
    "for",
    "from",
    "as",
    "more",
    "can",
    "be"
}

# Remove stopwords
filtered_words = [
    word
    for word in words
    if word not in stopwords
]

# Count again
filtered_counts = Counter(filtered_words)

# STEP 7: Meaningful top 10

print("\n===== TOP 10 AFTER STOPWORD REMOVAL =====")

for word, count in filtered_counts.most_common(10):
    print(f"{word}: {count}")

# STEP 8: Check an existing and missing word

print("\n===== COUNTER LOOKUP =====")

print("machine:", filtered_counts["machine"])
print("banana:", filtered_counts["banana"])