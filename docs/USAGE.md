# Usage Guide for Crypto Crew

This document provides step-by-step instructions on how to use the Crypto Crew project. It includes examples of running the project with different configurations, interpreting outputs, and troubleshooting common issues.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python version >=3.10 and <=3.13
- [Poetry](https://python-poetry.org/) for dependency management

## Installation

1. **Install Poetry** (if not already installed):

   ```bash
   pip install poetry
   ```

2. **Clone the Repository**:

   ```bash
   git clone https://github.com/teretzdev/cryptocrew.git
   cd cryptocrew
   ```

3. **Install Dependencies**:

   ```bash
   poetry install
   ```

## Configuration

The project is configured using YAML files located in the `src/crypto/config` directory:

- **agents.yaml**: Defines the agents and their roles.
- **tasks.yaml**: Specifies the tasks and their expected outputs.

Customize these files to suit your needs. For example, you can add new agents or tasks by modifying these YAML files.

## Running the Project

To run the project, use the following command from the root directory:

```bash
poetry run crypto
```

### Enabling Paper Trading Mode

To enable paper trading mode, set the `PAPER_TRADING` environment variable in your `.env` file:

```env
PAPER_TRADING=true
```

## Interpreting Outputs

The project generates reports and outputs based on the tasks defined in `tasks.yaml`. For example, a report on a specific cryptocurrency will be saved as a markdown file in the root directory.

## Troubleshooting

Here are some common issues and their solutions:

- **Missing Environment Variables**: Ensure all required environment variables are set in your `.env` file.
- **API Key Errors**: Verify that your Binance API keys are correct and have the necessary permissions.
- **Dependency Issues**: Run `poetry update` to ensure all dependencies are up-to-date.

## Environment Variables

The following environment variables are required:

- `BINANCE_API_KEY`: Your Binance API key.
- `BINANCE_SECRET_KEY`: Your Binance secret key.
- `OPENAI_API_KEY`: Your OpenAI API key.
- `PAPER_TRADING`: Set to `true` to enable paper trading mode.

Ensure these variables are set in your `.env` file. You can use the `.env.example` file as a template.

By following these instructions, you should be able to successfully configure and run the Crypto Crew project. For further assistance, refer to the project's [README.md](README.md) or contact support.
