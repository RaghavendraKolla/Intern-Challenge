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
Enter the genre (e.g., Action, Thriller, Comedy, Space): Action
Enter a description of the type of movies you like: Explosions and car chases 

Top Recommendations:
Title: The Vow (2012)
Description: After a car accident erases a woman’s memory, her husband fights to win her heart all over again.
Similarity Score: 0.257

Title: The Fog of War (2003)
Description: A deep look into war strategies and decision-making through the perspective of former U.S. Secretary of Defense Robert McNamara.
Similarity Score: 0.000

Title: The Pianist (2002)
Description: A Polish-Jewish pianist struggles to survive during World War II as he hides from the Nazis in war-torn Warsaw.
Similarity Score: 0.000

Title: The Pursuit of Happyness (2006)
Description: A struggling salesman fights through homelessness to build a better future for himself and his son.
Similarity Score: 0.000

Title: Dear John (2010)
Description: A soldier and a college student fall in love through letters, but the distance and war put their relationship to the test.
Similarity Score: 0.000
...



