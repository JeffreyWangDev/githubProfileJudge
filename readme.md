# GitHub Profile Judge

GitHub Profile Judge is a web application that evaluates GitHub profiles and provides a snarky rating based on the profile's content. It uses Google Generative AI to generate the responses.

## Features

- Evaluate GitHub profiles and receive a rating.
- Snarky and humorous responses.
- Dark mode support.
- Docker support for easy deployment.

## Installation

### Prerequisites

- Python 3.11
- Docker (optional, for containerized deployment)

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/githubProfileJudge.git
    cd githubProfileJudge
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your Google API key:

    ```sh
    echo "API_KEY=your_api_key_here" > .env
    ```

5. Run the application:

    ```sh
    python main.py
    ```

### Docker Deployment

1. Build the Docker image:

    ```sh
    docker build -t github-profile-judge .
    ```

2. Run the Docker container:

    ```sh
    docker run -p 80:80 github-profile-judge
    ```

## Usage

- Open your browser and go to `http://localhost`.
- Enter a GitHub username and click "Get Rating" to see the evaluation.

## License

This project is licensed under the MIT License.