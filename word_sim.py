import spacy
from scipy.spatial import distance

# Load the pre-trained GloVe model
nlp = spacy.load('en_core_web_md')

def get_word_vector(word):
    """Retrieve the vector representation of a word."""
    doc = nlp(word)
    if doc and doc.vector_norm != 0:
        return doc.vector
    else:
        return None

def cosine_similarity(vector1, vector2):
    """Calculate cosine similarity between two vectors."""
    return 1 - distance.cosine(vector1, vector2)

def main():
    # Input words
    word1 = input("Enter the first word: ").lower()
    word2 = input("Enter the second word: ").lower()

    # Get vectors
    vector1 = get_word_vector(word1)
    vector2 = get_word_vector(word2)

    if vector1 is None:
        print(f"The word '{word1}' is not in the vocabulary.")
        return
    if vector2 is None:
        print(f"The word '{word2}' is not in the vocabulary.")
        return

    # Calculate similarity
    similarity = cosine_similarity(vector1, vector2)

    # Display the result
    print(f"Cosine similarity between '{word1}' and '{word2}': {similarity:.4f}")

if __name__ == "__main__":
    main()
