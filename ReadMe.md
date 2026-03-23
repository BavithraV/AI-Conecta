pip install pre-commit detect-secrets

# create baseline
detect-secrets scan > .secrets.baseline

# install hooks
pre-commit install



##Gitleaks - brew install gitleaks (in terminal)