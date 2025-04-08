Smart Resume Matcher using NLTK is an NLP-based Python tool that helps job seekers compare their resumes against job descriptions. It highlights missing keywords, suggests improvements, and provides a match score — all using fundamental NLP techniques powered by NLTK.

This project was built to:

Practice core NLP tasks like tokenization, lemmatization, and similarity scoring.

Solve a real-world problem that many job seekers face: aligning resumes with job requirements.


#### What makes this project meaningful:
Uses pure NLTK — no external ML/AI APIs

Solves a practical problem — helps improve resume-job alignment

Shows cosine similarity between resume and job description

Identifies missing or underused keywords in the resume

Fully contained in one clean script and easy to run

##### Skills Demonstrated
##### Text preprocessing :
Text preprocessing is the foundational step in NLP. In this project, we applied several preprocessing techniques to clean and normalize the input resume and job description text:

Lowercasing: Converts all text to lowercase to ensure consistency (e.g., "Python" and "python" are treated the same).

Stopword Removal: Common words like “the,” “is,” “and,” etc., don’t contribute to meaning in NLP tasks, so we remove them using NLTK’s stopword list.

Lemmatization: Reduces words to their base/root form (e.g., "running" → "run"). We used NLTK’s WordNet Lemmatizer for this.

✅ This ensures we’re working with meaningful, standardized tokens before any analysis.

#### Tokenization & frequency analysis:
Once the text is cleaned, we tokenize it — meaning we break it into individual words (tokens) using nltk.word_tokenize().

After tokenizing:

We use collections.Counter to count how many times each word appears.

These word frequency dictionaries are then used to build feature vectors for each text.

✅ Frequency analysis lets us numerically compare text content in a meaningful way.

#### Cosine similarity from scratch:
Instead of using a pre-built ML library, we implemented cosine similarity ourselves using Python’s math module.

Cosine similarity calculates the angle between two frequency vectors.

A smaller angle (i.e., higher cosine value) means the resume and job description are more similar.

Formula used:  Cos(tita)=A.B/(||A|| . ||B||)

Where A and B are frequency vectors of the resume and job description.

✅ This shows an understanding of both linear algebra and vector space models in NLP.

#### Working with file I/O in Python:
We used Python’s built-in file handling methods to:

Load the resume and job description from .txt files.

Support flexible input for real-world usage (can swap in any resume or JD).

#### Building reusable, modular code:
Though this project is in a single file, it’s structured into modular functions:

preprocess_text() – handles all text cleaning

cosine_similarity() – performs the vector math

load_and_process() – handles file reading + preprocessing

main() – coordinates everything cleanly

✅ This design makes the code readable, testable, and scalable for future improvements.

#### Explaining NLP workflows clearly:
In this project, I documented each major NLP step and added comments throughout the code to explain why each step is important.

Additionally:

The project README provides a clear walkthrough of the logic.

Output is printed in an intuitive way (match % and suggestions).

✅ Clear communication of NLP pipelines is crucial when working in teams or applying for roles that require explainability.

