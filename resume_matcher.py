import nltk
import string
import math
from collections import Counter

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# ---- Preprocessing Function ---- #
def preprocess_text(text):
    # Lowercase
    text = text.lower()

    # Tokenize
    tokens = nltk.word_tokenize(text)

    # Remove stopwords and punctuation, lemmatize
    clean_tokens = []
    for token in tokens:
        if token not in stop_words and token not in string.punctuation:
            lemma = lemmatizer.lemmatize(token)
            clean_tokens.append(lemma)

    return clean_tokens

# ---- Cosine Similarity Function ---- #
def cosine_similarity(vec1, vec2):
    intersection = set(vec1) & set(vec2)

    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1])
    sum2 = sum([vec2[x] ** 2 for x in vec2])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return round((numerator / denominator) * 100, 2)

# ---- Load and Process Text ---- #
def load_and_process(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        raw_text = file.read()
        tokens = preprocess_text(raw_text)
        return tokens

# ---- Main Logic ---- #
def main():
    # Load files
    resume_tokens = load_and_process("C:/Users/ohars/NLP/resume.txt")
    jd_tokens = load_and_process("C:/Users/ohars/NLP/job_description.txt")

    # Create frequency vectors
    resume_freq = Counter(resume_tokens)
    jd_freq = Counter(jd_tokens)

    # Compute cosine similarity
    similarity = cosine_similarity(resume_freq, jd_freq)

    # Identify missing keywords from JD
    missing_keywords = [word for word in set(jd_tokens) if word not in resume_tokens]

    # Output
    print("\n🔍 Resume-JD Match Score:", similarity, "%")
    print("\n📌 Keywords in Job Description missing from Resume:")
    for keyword in sorted(set(missing_keywords))[:20]:  # limit to 20
        print(" -", keyword)

    # Suggest edits
    if similarity < 60:
        print("\n⚠️  Consider adding more relevant keywords or projects to your resume.")
    else:
        print("\n✅ Your resume matches the job description quite well!")

if __name__ == "__main__":
    main()
