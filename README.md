# better-cdk-python
Boilerplate template for Python CDK, better than what `cdk init` gets you. 

## Boilerplate Features 
- Built-in loading of Lambda environment variables
- Local packaging of Lambda code & dependencies
- `pyproject.toml` instead of `requirements.txt`
- Commented-out examples of common infrastructure
- Linting with [Ruff](https://docs.astral.sh/ruff/)
- Package management with [uv](https://docs.astral.sh/uv/)

## Prerequisites
1. Ensure you have the [AWS CLI](https://aws.amazon.com/cli/) installed.
2. Ensure you have [uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) installed.
2. Update the `pyproject.toml` with your project's information.
3. Run `cp .env.sample .env` and put your Lambda environment variables in the newly created `.env`. 
4. Export your AWS account information to your shell as outlined [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-set).
5. To install dependencies, run:
```
python3 -m venv .venv
source .venv/bin/activate
uv pip install -r pyproject.toml
```

## Deploying
To see a CDK diff for the deployment, run `cdk diff`. Otherwise, run `cdk synth && cdk deploy`.