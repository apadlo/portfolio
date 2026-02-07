# Branch Protection Guidelines

## Main Branch Protection

This repository implements automated checks to protect the main branch and ensure code quality.

## Required Checks

All pull requests to the `main` branch must pass the following automated checks:

### 1. Code Quality Checks
- **Black**: Code formatting validation
- **Flake8**: Linting to catch common errors
- **Pylint**: Static code analysis

### 2. Python Syntax Check
- Validates Python syntax
- Checks dependency compatibility

### 3. Security Vulnerability Scan
- Scans dependencies for known security vulnerabilities
- Uses `safety` to check against vulnerability databases

### 4. Test Application Build
- Validates application imports
- Checks file structure integrity

## Setting Up Branch Protection Rules

To fully protect the main branch, repository administrators should configure the following settings in GitHub:

1. Go to **Settings** → **Branches** → **Branch protection rules**
2. Click **Add rule** and set the branch name pattern to `main`
3. Enable the following options:

   ✅ **Require a pull request before merging**
   - Require approvals: 1 (recommended)
   - Dismiss stale pull request approvals when new commits are pushed

   ✅ **Require status checks to pass before merging**
   - Require branches to be up to date before merging
   - Status checks that are required:
     - `Code Quality Checks`
     - `Python Syntax Check`
     - `Security Vulnerability Scan`
     - `Test Application Build`
     - `All Checks Passed`

   ✅ **Require conversation resolution before merging**

   ✅ **Do not allow bypassing the above settings**

   ⚠️ **Include administrators** (recommended for strict protection)

## Workflow Details

The CI workflow (`.github/workflows/ci.yml`) runs automatically on:
- Pull requests targeting the `main` branch
- Direct pushes to the `main` branch

## Local Development

Before creating a pull request, developers should:

1. **Format code**:
   ```bash
   pip install black
   black app.py
   ```

2. **Run linting**:
   ```bash
   pip install flake8
   flake8 app.py --max-line-length=120
   ```

3. **Check security**:
   ```bash
   pip install safety
   safety check
   ```

4. **Test the application**:
   ```bash
   streamlit run app.py
   ```

## Benefits

- 🛡️ Prevents breaking changes from being merged
- ✅ Ensures consistent code quality
- 🔒 Identifies security vulnerabilities early
- 📝 Maintains code standards across the project
- 🔄 Automates review processes

## Support

For questions or issues with the CI/CD pipeline, please open an issue in the repository.
