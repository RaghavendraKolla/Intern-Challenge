# Movie Recommendation System

## Dataset
The dataset used for this project is `movies.csv`, which contains movie titles and descriptions. To load it, the program reads the CSV file using pandas:

```python
import pandas as pd
data = pd.read_csv("movies.csv")
```

Ensure the dataset is placed in the same directory as the script or provide the correct path in the `load_dataset()` function.

## Setup
### Requirements
- Python 3.x
- Virtual Environment (Recommended)

### Setup Instructions
1. **Create and activate a virtual environment:**  
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
2. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```

## Running the Program
To run the recommendation system, execute the script with:

```sh
python AI_ML\ Program.py
```

It will prompt you to enter:
- A preferred genre (e.g., Action, Thriller, Comedy).
- A description of the type of movies you like.

The system then recommends movies based on similarity scores.

## Results
Example output for a sample query:

```
Enter a description of the type of movies you like: I love thrilling action movies set in space, with a comedic twist.

Top Recommendations:
Title: Prisoners (2013)
Description: When two children go missing, a father takes matters into his own hands while the police follow a set of clues.
Similarity Score: 0.108

Title: WALL-E (2008)
Description: A lonely waste-collecting robot on an abandoned Earth embarks on a space adventure that could save humanity.
Similarity Score: 0.104

Title: Toy Story (1995)
Description: A cowboy doll feels threatened when a new astronaut action figure becomes his owner’s favorite toy.
Similarity Score: 0.086

Title: Free Solo (2018)
Description: A thrilling, Oscar-winning documentary following rock climber Alex Honnold as he attempts to free-climb El Capitan without any ropes.
Similarity Score: 0.084

Title: Groundhog Day (1993)
Description: A cynical TV weatherman finds himself reliving the same day over and over again, leading to comedic self-discovery and personal growth.
Similarity Score: 0.069
...




