# Semantic Showdown

**Semantic Showdown** is a word-guessing game where teams compete to guess words most similar to a target word. The game uses word embeddings and cosine similarity to score guesses, making it a fun and educational tool for understanding semantic relationships between words.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.8 or higher
- Conda (for environment management)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/semantic-showdown.git
   cd semantic-showdown
   ```

2. **Create and Activate the Conda Environment:**
   ```bash
   conda env create -f environment.yml
   conda activate semantic_showdown
   ```

3. **Install Required Packages:**
   ```bash
   conda install spacy scipy
   python -m spacy download en_core_web_md
   ```

## Usage

### Running the Game

1. **Start the Game:**
   ```bash
   python semantic_showdown.py
   ```

2. **Follow the Prompts:**
   - Enter the target word for each team's turn.
   - Input guessed words when prompted.
   - The game will calculate similarities and update scores accordingly.

### Content Files

- **`semantic_showdown.py`**: The main game script.
- **`environment.yml`**: Conda environment configuration file.

## Game Rules

1. **Setup:**
   - The host chooses a target word at the beginning of each team's turn.
   - Two teams compete, each taking turns.

2. **Turn Mechanics:**
   - Each team has 5 turns.
   - During a turn, the team can guess words until they score 5 validations or 3 strikes.
   - A validation occurs if the cosine similarity between the guessed word and the target word is above a threshold (default 0.5).
   - A strike occurs if the guessed word is not validated.

3. **Scoring:**
   - Each validation scores +1 point.
   - The team with the most points after all turns wins.
   - If both teams have the same score, it's a tie.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy playing **Semantic Showdown** and have fun exploring the semantic relationships between words!
