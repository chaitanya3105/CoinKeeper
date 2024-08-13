# CoinKeeper

**Brief Description:**  
CoinKeeper is a personal finance tracker designed to help you manage your finances with ease. Whether you're tracking your daily expenses, setting budget goals, or planning for future savings, CoinKeeper provides the tools to monitor your financial health effectively.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)


## Features

- **Real-Time Tracking**: Monitor your income and expenses in real-time.
- **Budget Management**: Set, track, and adjust your budget goals.
- **Financial Insights**: Receive personalized tips and insights based on your financial data.
- **Interactive Visualizations**: Visualize your financial trends with dynamic charts.
- **User-Friendly Interface**: Simple and intuitive design for ease of use.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/CoinKeeper.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd CoinKeeper
    ```
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

## Usage

- **Run the development server**:
    ```bash
    python manage.py runserver
    ```
- **Access the application**: Open your web browser and navigate to `http://localhost:8000`.
- **Sign Up / Log In**: Create an account or log in to start managing your finances.

## Screenshots

![Dashboard Screenshot](coinkeeper1)  
*Dashboard Overview*

![Transactions Screenshot](coinkeeper2)  
*View and manage your transactions easily.*

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS (TailwindCSS)
- **Database**: SQLite (default), PostgreSQL (optional)
- **Other**: HTMX for dynamic interactions

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature-branch
    ```
3. **Commit your changes**:
    ```bash
    git commit -m "Add new feature"
    ```
4. **Push to the branch**:
    ```bash
    git push origin feature-branch
    ```
5. **Open a Pull Request**.


