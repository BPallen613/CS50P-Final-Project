# Python Wordle

### Description:
This program is a Wordle game where the user has up to six attempts to guess a five-letter word randomly selected from the CSV file `wordles.csv`.

### How the Program Works:
### Libraries Used:
**csv:** To read the list of 5 letter words from a CSV file.

**random:** To randomly select a word from the list.

**tabulate:** To format the game output in a readable table.

**tabulate[widechars]:** To format table with emojis

**sys:** To handle potential file errors and exit the program if necessary.
<br/>
<br/>

### Key Steps in the Program:

**Open CSV File:** The program reads the `wordles.csv` file to get the list of potential words.

**Select Random Word:** A random word is chosen from the CSV file using the random library.

**Game Loop:** The user has up to six attempts to guess the word. For each guess, the program checks if the input is a valid five-letter word.The program provides feedback on each guess, indicating correct letters (🟢), misplaced letters (🟡), and incorrect letters (🔴).The game ends if the user correctly guesses the word or fails on all 6 attempts.

**Output:** The game progress is displayed using the tabulate library to format the output as a table.
<br/>
<br/>

### TODO

**Download the Repository:** Clone the repository or download the ZIP file.
```
git clone https://github.com/BPallen613/CS50P-Final-Project.git
```
**Navigate to the Project Directory:**
```
cd CS50P-Final-Project
```
**Install Required Libraries:**
```
pip install -r requirements.txt
```
**Run the Program:**
```
python project.py
```
**Test the Program:**
```
pytest test_project.py
```
<br/>
<br/>

### Functions

**Main Function:**

**Opening CSV File:** Uses the `csv` and `sys` libraries. The function attempts to open `wordles.csv` with `csv` to gain access to all the 5-letter words within the CSV. It then gets appended into a table for future use. If the function cannot open the CSV file, `sys` is used to exit the program.

**Tracker:** Is used for the `tabulate` output after each guess. It has the headers appended instantly. After each guess, the guessed word, the attempt number, and letter checks are appended to the list.

**While Loop:** Keeps the game going until either the player has won or has maxed out their 6 attempts.

**For Loop:** Checks if the guess is a word. If it is not a word, the user has to re-enter their guess.
<br/>
<br/>

**get_random:** Uses the `random.randrange` feature in the `random` library. The random range is between 1 and 5757 as the `wordles.csv` contains 5757 words in it. This provides a random word that will be used in the `get_word` function.
<br/>
<br/>

**get_word:** Table and n variables are passed into the `get_word` function so it can find the wordle within the list. Once it has the wordle, it is returned to the `main` function.
<br/>
<br/>

**guess:** Collects the inputted guesses from the user.
<br/>
<br/>

**check_length_alpha:** Verifies that the user has entered a string that is 5 letters long, ensuring that all characters are letters.
<br/>
<br/>

**validate:** Creates the track string for tracker output. It validates each letter on if it is correct placement, exists in the word, or is non-existent. Returns track to the `main` function to later get appended to the tracker function.
<br/>
<br/>

**round_attempts:** Increases the attempts after each round.

<br/>
<br/>

**Note** Not all 5 letter English words are included.

## References
[csv library](https://docs.python.org/3/library/csv.html)

[random library](https://docs.python.org/3/library/random.html)

[tabulate library](https://pypi.org/project/tabulate/)

[sys library](https://docs.python.org/3/library/sys.html)
