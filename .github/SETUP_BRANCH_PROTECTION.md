# Setting Up Branch Protection Rules

This guide explains how to enable branch protection for the `main` branch in GitHub.

## Overview

This repository includes automated CI/CD workflows that run on every pull request. To fully protect the main branch, you need to configure branch protection rules in GitHub's repository settings.

## Step-by-Step Instructions

### 1. Navigate to Repository Settings

1. Go to your repository: `https://github.com/apadlo/portfolio`
2. Click on **Settings** (gear icon in the top navigation)
3. In the left sidebar, click **Branches**

### 2. Add Branch Protection Rule

1. Click the **Add rule** button (or **Add branch protection rule**)
2. In the "Branch name pattern" field, enter: `main`

### 3. Configure Protection Settings

Enable the following settings:

#### Require a pull request before merging
- ✅ Check "Require a pull request before merging"
- Set "Required number of approvals before merging": **1** (recommended)
- ✅ Check "Dismiss stale pull request approvals when new commits are pushed"
- ✅ Check "Require review from Code Owners" (optional but recommended)

#### Require status checks to pass before merging
- ✅ Check "Require status checks to pass before merging"
- ✅ Check "Require branches to be up to date before merging"
- In the search box, add these required status checks:
  - `Code Quality Checks`
  - `Python Syntax Check`
  - `Security Vulnerability Scan`
  - `Test Application Build`
  - `All Checks Passed`

**Note**: Status checks will only appear in the list after they have run at least once. Create a test PR to trigger the workflows first.

#### Require conversation resolution before merging
- ✅ Check "Require conversation resolution before merging"

#### Additional settings (optional but recommended)
- ✅ Check "Require linear history" (keeps commit history clean)
- ✅ Check "Do not allow bypassing the above settings"
- ✅ Check "Include administrators" (applies rules to admins too)

### 4. Save Changes

Click **Create** or **Save changes** at the bottom of the page.

## What This Protects Against

With these settings enabled:

1. ❌ **No direct pushes to main** - All changes must go through pull requests
2. ✅ **Code review required** - At least one approval needed before merging
3. ✅ **Automated quality checks** - All CI tests must pass
4. ✅ **Security validation** - Dependencies are scanned for vulnerabilities
5. ✅ **Conversation resolution** - All review comments must be addressed

## Testing the Protection

To verify branch protection is working:

1. Try to push directly to main (should be blocked)
2. Create a PR with intentionally broken code (CI should fail)
3. Create a PR with working code (CI should pass, review required)

## Troubleshooting

### Status checks don't appear in the list
- The checks must run at least once before they appear
- Create a test pull request to trigger the workflows
- After the workflows run, return to branch protection settings

### Can't push to main anymore
- This is expected! Create a branch and open a pull request instead
- Use: `git checkout -b feature/your-feature`

### CI checks are failing
- Review the workflow logs in the Actions tab
- Fix the issues locally before pushing
- See [Contributing Guidelines](.github/CONTRIBUTING.md) for code quality tools

## Additional Resources

- [GitHub Branch Protection Documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [About Required Status Checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)
- [About Code Owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)

## Support

If you need help setting up branch protection, feel free to open an issue in the repository.
