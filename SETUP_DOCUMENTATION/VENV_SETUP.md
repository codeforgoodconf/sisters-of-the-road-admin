# Set up Python Environment using venv

1. Set up a [Python virtual environment](https://docs.python.org/3/library/venv.html). 
You can name it anything you like, but keep it short, lowercase, without any special characters.
    
    ```bash
    python -m venv myvenv
    ```

2. Activate the virtual environment.

    - On Mac/Linux:
    ```sh
    source myvenv/bin/activate
    ```
    
    - On Windows:
    ```sh
    myvenv\Scripts\activate
    ```

3. Install the Python dependencies.

    ```sh
    pip install -r requirements.txt
    ```