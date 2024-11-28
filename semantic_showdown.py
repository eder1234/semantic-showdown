import spacy
from scipy.spatial.distance import cosine

# Load the pre-trained GloVe model
nlp = spacy.load('en_core_web_md')

# Function to calculate cosine similarity between two word vectors
def calculate_similarity(word1, word2):
    vector1 = nlp(word1.lower()).vector
    vector2 = nlp(word2.lower()).vector
    return 1 - cosine(vector1, vector2)

# Team class to keep track of team scores
class Team:
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def add_points(self, points):
        self.total_score += points

# Game class to manage the game flow
class SemanticShowdown:
    def __init__(self, team1, team2, threshold=0.5):
        self.team1 = team1
        self.team2 = team2
        self.threshold = threshold

    def play_turn(self, team, target_word):
        validations = 0
        strikes = 0
        print(f"\n{team.name}'s turn:")
        while validations < 5 and strikes < 3:
            guessed_word = input("Enter guessed word: ").strip().lower()
            if not guessed_word:
                print("Please enter a valid word.")
                continue
            if guessed_word == target_word:
                print("Exact match! Automatically validated.")
                validations += 1
                continue
            similarity = calculate_similarity(guessed_word, target_word)
            if similarity == -1:
                print("Word not in vocabulary. Strike!")
                strikes += 1
            elif similarity >= self.threshold:
                print(f"Similarity: {similarity:.4f}. Validated!")
                validations += 1
            else:
                print(f"Similarity: {similarity:.4f}. Strike!")
                strikes += 1
        team.add_points(validations)
        print(f"{team.name}'s turn ended with {validations} validations and {strikes} strikes.")
        print(f"Total score: {team.total_score}")

    def play_game(self):
        for _ in range(5):
            target_word_team1 = input(f"Enter target word for {self.team1.name}'s turn: ").strip().lower()
            self.play_turn(self.team1, target_word_team1)
            target_word_team2 = input(f"Enter target word for {self.team2.name}'s turn: ").strip().lower()
            self.play_turn(self.team2, target_word_team2)
        if self.team1.total_score > self.team2.total_score:
            print(f"\n{self.team1.name} wins with a score of {self.team1.total_score} to {self.team2.total_score}!")
        elif self.team2.total_score > self.team1.total_score:
            print(f"\n{self.team2.name} wins with a score of {self.team2.total_score} to {self.team1.total_score}!")
        else:
            print(f"\nIt's a tie! Both teams scored {self.team1.total_score} points.")

# Main function to start the game
def main():
    print("Welcome to Semantic Showdown!")
    team1_name = input("Enter Team 1 name: ").strip()
    team2_name = input("Enter Team 2 name: ").strip()
    threshold = float(input("Enter similarity threshold (default 0.5): ") or 0.5)
    team1 = Team(team1_name)
    team2 = Team(team2_name)
    game = SemanticShowdown(team1, team2, threshold)
    game.play_game()

if __name__ == "__main__":
    main()
