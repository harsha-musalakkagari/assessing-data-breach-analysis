# Assessing Data Breach Factors Through Modern Crime Theory

## Project Overview

This project focuses on assessing data breach factors using modern crime theory. It provides a web-based Django application for working with data breach information and examining factors associated with data breaches.

## Technologies Used

- **Programming Language:** Python
- **Backend Framework:** Django
- **Database:** MySQL
- **Data Analysis:** Pandas, NumPy, Scikit-learn
- **Frontend:** HTML, CSS, JavaScript

## Project Structure

- `Data_Analytics/` – Data analytics-related files
- `Remote_User/` – Remote user module
- `Service_Provider/` – Service provider module
- `Template/` – HTML templates
- `assessing_data_breach/` – Django project configuration
- `Datasets.csv` – Dataset
- `Results.csv` – Results data
- `manage.py` – Django management script

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd assessing_data_breach
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and configure the following variables using your own local credentials:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
```

Never upload your `.env` file to GitHub.

### 6. Run database migrations

```bash
python manage.py migrate
```

### 7. Start the Django server

```bash
python manage.py runserver
```

Open your browser at:

`http://127.0.0.1:8000/`

## Author

**Harsha Vardhan Musalakkagari**