# Digital CV Portfolio

[![CI - Main Branch Protection](https://github.com/apadlo/portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/apadlo/portfolio/actions/workflows/ci.yml)

A modern, interactive digital CV/portfolio built with Streamlit, showcasing professional experience, skills, and projects.

## 🌟 Features

- **Interactive Web Interface**: Clean and professional Streamlit-based UI with custom styling
- **Downloadable Resume**: PDF resume available for download
- **Project Showcase**: Links to various automation and testing projects
- **Work History Timeline**: Comprehensive career history with detailed descriptions
- **Skills Overview**: Organized display of technical skills and competencies
- **Contact Integration**: Easy contact via email and LinkedIn

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/apadlo/portfolio.git
cd portfolio
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 🛠️ Technology Stack

- **Framework**: Streamlit
- **Language**: Python
- **Libraries**: 
  - Pillow (PIL) for image handling
  - Pandas for data processing
  - Various Streamlit components

## 📁 Project Structure

```
portfolio/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml       # Streamlit theme configuration
├── assets/
│   ├── CV.pdf            # Resume PDF
│   └── profile-pic.png   # Profile picture
└── styles/
    └── main.css          # Custom CSS styles
```

## 🎨 Customization

The application uses a custom theme defined in `.streamlit/config.toml`. You can modify the colors and styling to match your preferences.

## 🛡️ Branch Protection

This repository implements automated CI/CD checks to protect the main branch:
- Code quality validation (Black, Flake8, Pylint)
- Python syntax checking
- Security vulnerability scanning
- Application build testing

See [Branch Protection Guidelines](.github/BRANCH_PROTECTION.md) for more details.

## 🤝 Contributing

Contributions are welcome! Please see our [Contributing Guidelines](.github/CONTRIBUTING.md) for details on how to get started.

## 📫 Contact

**Andrzej Padło**
- LinkedIn: [andrzejpadlo](https://www.linkedin.com/in/andrzejpadlo/)
- Email: apadlo@hotmail.com

## 📝 License

This project is open source and available for personal and educational use.

## 🏆 Featured Projects

This portfolio showcases several automation testing frameworks and projects:
- Playwright Python Framework
- Python Selenium Framework
- Python Backend Testing Framework
- Python Appium Framework
- Django Testing with Pytest
- AI-powered Applications

Visit the live application to explore all projects and detailed work history.
