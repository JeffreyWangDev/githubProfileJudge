# GitHub Profile Judge

GitHub Profile Judge is a web application that evaluates GitHub profiles and provides a snarky rating based on the profile's content.

# [Demo](https://gpr.jeffrey.hackclub.app/)
![image](https://github.com/user-attachments/assets/be1fea15-ee41-4c63-885a-2fc1d43d3130)


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
    git clone https://github.com/jeffreywangdev/githubProfileJudge.git
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
<img width="583" alt="image" src="https://github.com/user-attachments/assets/17406795-c15b-4e76-91ce-283f49409145">
