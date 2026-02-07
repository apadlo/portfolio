# Contributing to Digital CV Portfolio

Thank you for considering contributing to this project! 🎉

## Code of Conduct

Please be respectful and constructive in all interactions.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue using the Bug Report template and include:
- A clear description of the bug
- Steps to reproduce
- Expected vs. actual behavior
- Your environment details

### Suggesting Features

Feature requests are welcome! Please use the Feature Request template and explain:
- The problem you're trying to solve
- Your proposed solution
- Any alternatives you've considered

### Pull Requests

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines

3. **Test your changes locally**
   ```bash
   streamlit run app.py
   ```

4. **Format and lint your code** (if modifying Python files)
   ```bash
   pip install black flake8
   black app.py
   flake8 app.py --max-line-length=120
   ```

5. **Commit your changes** with a clear commit message
   ```bash
   git commit -m "Add: brief description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request** against the `main` branch

## Development Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation
```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/portfolio.git
cd portfolio

# Install dependencies
pip install -r requirements.txt

# Install development tools
pip install black flake8 pylint safety
```

### Running the Application
```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## Code Style Guidelines

- Follow PEP 8 style guidelines
- Use Black for code formatting (max line length: 120)
- Write clear, descriptive variable and function names
- Add comments for complex logic
- Keep functions focused and concise

## Branch Protection & CI

All pull requests to `main` must pass automated checks:

- ✅ **Code Quality**: Black, Flake8, Pylint
- ✅ **Syntax Check**: Python syntax validation
- ✅ **Security Scan**: Dependency vulnerability checks
- ✅ **Build Test**: Application import and structure validation

See [Branch Protection Guidelines](.github/BRANCH_PROTECTION.md) for details.

## Pull Request Guidelines

- Fill out the pull request template completely
- Keep changes focused and minimal
- Include a clear description of what and why
- Reference any related issues
- Ensure all CI checks pass
- Be responsive to review feedback

## Testing

Before submitting a PR:

1. Test the application locally
2. Verify all imports work
3. Check that the UI renders correctly
4. Run code quality tools

## Questions?

Feel free to open an issue for questions or discussions.

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing! 🙏
