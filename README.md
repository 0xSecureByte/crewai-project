# Travel Planner Crew

A Django-based application to help users plan their travels by selecting cities, providing local insights, and creating detailed itineraries.

## Features

- **City Selection**: Choose the best city based on weather, events, and costs.
- **Local Insights**: Get guides and recommendations for attractions and customs.
- **Travel Itineraries**: Create 7-day travel plans with schedules and budgets.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/travel-planner-crew.git
   cd travel-planner-crew
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file and add your API keys:
   ```
   BROWSERLESS_API_KEY=your_browserless_api_key
   SERPER_API_KEY=your_serper_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

## Usage

- **Web Interface**: Access via `http://localhost:8000`.
- **Command Line**: Use `main.py` for CLI operations.

## Contributing

Fork the repository and submit a pull request for improvements or bug fixes.

## License

Licensed under the MIT License.