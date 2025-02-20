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
Title: Mad Max: Fury Road  
Description: A post-apocalyptic action movie with high-speed chases, explosions, and intense battles.  
Similarity Score: 0.845  

Title: Die Hard  
Description: A thrilling action-packed movie with gunfights and explosions.  
Similarity Score: 0.812  
...



