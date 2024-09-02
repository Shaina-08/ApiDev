# FastAPI CRUD Operations

This repository contains a CRUD (Create, Read, Update, Delete) application built using [FastAPI](https://fastapi.tiangolo.com/). The application demonstrates RESTful API endpoints for managing posts, such as creating, retrieving, updating, and deleting posts.

## Features

- **Create**: Add a new post.
- **Read**: Retrieve all posts or a specific post by its ID.
- **Update**: Modify an existing post.
- **Delete**: Remove a post by its ID.
- **Get Latest Post**: Retrieve the latest created post.

## Getting Started

### Prerequisites

- **Python 3.12+**: Ensure Python is installed. Download it from [python.org](https://www.python.org/downloads/).
- **pip3**: The Python package installer, usually included with Python.

### Installation

To set up and run the FastAPI application, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Shaina-08/ApiDev.git
    cd ApiDev
    ```

2. **Create a virtual environment** (recommended):

    ```bash
    python3 -m venv venv
    ```

    This command creates a virtual environment named `venv`. You can choose a different name if you prefer.

3. **Activate the virtual environment**:

    - **On macOS/Linux**:

      ```bash
      source venv/bin/activate
      ```

    - **On Windows**:

      ```bash
      venv\Scripts\activate
      ```

    Activating the virtual environment ensures that you are using the Python interpreter and packages from the virtual environment rather than the global Python installation.

4. **Install the dependencies**:

    Ensure that you have `pip3` installed, and then run:

    ```bash
    pip3 install fastapi uvicorn
    ```

    If you have a `requirements.txt` file with all dependencies listed, you can install them using:

    ```bash
    pip3 install -r requirements.txt
    ```

5. **Run the FastAPI application**:

    ```bash
    uvicorn app.main:app --reload
    ```

    This will start the development server, and the API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints

- **GET /**: Root endpoint that returns a welcome message.

    ```bash
    curl -X 'GET' 'http://127.0.0.1:8000/' -H 'accept: application/json'
    ```

- **GET /posts**: Retrieve all posts.

    ```bash
    curl -X 'GET' 'http://127.0.0.1:8000/posts' -H 'accept: application/json'
    ```

- **GET /posts/{id}**: Retrieve a specific post by its ID.

    ```bash
    curl -X 'GET' 'http://127.0.0.1:8000/posts/1' -H 'accept: application/json'
    ```

- **GET /posts/latest**: Retrieve the latest post.

    ```bash
    curl -X 'GET' 'http://127.0.0.1:8000/posts/latest' -H 'accept: application/json'
    ```

- **POST /posts**: Create a new post. Requires a JSON body with `title`, `content`, `published` (optional), and `rating` (optional).

    ```bash
    curl -X 'POST' \
      'http://127.0.0.1:8000/posts' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
        "title": "New Post",
        "content": "This is the content of the new post",
        "published": true
      }'
    ```

- **DELETE /posts/{id}**: Delete a post by its ID.

    ```bash
    curl -X 'DELETE' 'http://127.0.0.1:8000/posts/1' -H 'accept: application/json'
    ```

- **PUT /posts/{id}**: Update an existing post. Requires a JSON body with updated `title`, `content`, `published` (optional), and `rating` (optional).

    ```bash
    curl -X 'PUT' \
      'http://127.0.0.1:8000/posts/1' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
        "title": "Updated Post Title",
        "content": "Updated content",
        "published": false
      }'
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
