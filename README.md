# Streamlit Starter

A template for a dynamic single-page web application using Streamlit.

## Features

- **Modular Design**: Organized directory structure for easy management of components.
- **Pre-built Components**: Includes header, footer, sidebar, and main content area in `app/ui/components/`.
- **API Integration**: Example in `app/ui/actions/api.py` for fetching and displaying data.
- **Customizable Styling**: Modify `assets/css/style.css` to change the appearance.
- **Logging Support**: Uses `loguru` for logging.
- **Streamlit Configuration**: Optimized settings in `app/app.py`.
- **Docker Support**: Includes a Dockerfile for deployment.

## Getting Started

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/streamlit-cutter.git
   cd streamlit-starter
   ```

2. **Install Dependencies**

   Make sure Python is installed, then run:

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```sh
   streamlit run app/app.py
   ```

4. **Customize**

   Explore the `app/` directory to add new components, styles, or API integrations.

   ```plaintext
   .
   |-- .env.example
   |-- .gitignore
   |-- app/
   |   |-- app.py
   |   |-- assets/
   |   |   |-- css/
   |   |   |   `-- style.css
   |   |   `-- images/
   |   |-- layout.py
   |   `-- ui/
   |       |-- actions/
   |       |   `-- api.py
   |       `-- components/
   |           |-- footer.py
   |           |-- header.py
   |           |-- main.py
   |           `-- sidebar.py
   |-- Dockerfile
   |-- README.md
   `-- requirements.txt
   ```

## Contributing

Contributions and feedback are welcome.
