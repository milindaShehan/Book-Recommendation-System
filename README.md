# Book Recommendation System

This Book Recommendation System suggests books based on a selected title, displaying recommended titles along with their cover images.

## Project Structure

- **app.py**: The main Streamlit application file.
- **artifacts/**: Directory containing pre-trained models and data files.
    - `modal.pkl`: Pre-trained model for book recommendations.
    - `books_name.pkl`: List of book names for the recommendation selection.
    - `final_rating.pkl`: Dataframe with book ratings and image URLs.
    - `book_pivot.pkl`: Book-pivot table for recommendation calculations.

## Setup and Installation

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Streamlit](https://streamlit.io/)

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/Book-Recommendation-System.git
    cd Book-Recommendation-System
    ```

2. **Install dependencies**:
    Ensure that `requirements.txt` is in the project directory, then run:
    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure all required data files are in place**:
    Place the following files in an `artifacts` folder:
    - `modal.pkl`
    - `books_name.pkl`
    - `final_rating.pkl`
    - `book_pivot.pkl`

4. **Run the Streamlit app**:
    Start the app by running:
    ```bash
    streamlit run app.py
    ```

5. **Using the Application**:
    - Open the provided local URL in your browser.
    - Select a book from the dropdown menu and click **Recommend** to see book suggestions with their cover images.

## Troubleshooting

- If you encounter a `FileNotFoundError` for any `.pkl` files, ensure they are in the correct path (`artifacts` folder).
- If dependencies fail to install, confirm that `requirements.txt` is correctly configured and contains all necessary packages.

## Requirements

List of primary dependencies (included in `requirements.txt`):
- `streamlit`
- `numpy`
- `pickle` (built-in to Python)
- Other dependencies required for model loading and data handling

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset and resources for the recommendation system.
- Streamlit documentation and community for guidance.
