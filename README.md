# Crypto Crew

Welcome to the Crypto Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
## Configuration

The project is configured using YAML files located in the `src/crypto/config` directory. The `agents.yaml` file defines the agents and their roles, while the `tasks.yaml` file specifies the tasks and their expected outputs. Customize these files to suit your needs.

## Customizing

## Paper Trading Option

To enable paper trading mode, set the `PAPER_TRADING` environment variable to `True`. This will connect the application to Binance's testnet, allowing you to simulate trades without using real funds. Follow these steps to set up paper trading:

1. Obtain Binance Testnet API keys by registering at [Binance Testnet](https://testnet.binance.vision/).
2. Update the `.env` file with your testnet API keys:
   ```
   BINANCE_API_KEY=your_testnet_api_key_here
   BINANCE_SECRET_KEY=your_testnet_secret_key_here
   ```
3. Set the `PAPER_TRADING` environment variable to `True` in your `.env` file or your environment:
   ```
   PAPER_TRADING=True
   ```

When `PAPER_TRADING` is not set or set to `False`, the application will use the live trading environment with real funds. Ensure you have the correct API keys for the mode you are using to prevent any authentication issues.

## Contributing

We welcome contributions from the community! To contribute, please fork the repository, make your changes, and submit a pull request. Ensure your code adheres to the project's coding standards and includes appropriate tests.

**Add your `OPENAI_API_KEY` into the `.env` file**. This key is required for the project to interact with OpenAI's API.

- Modify `src/crypto/config/agents.yaml` to define your agents
- Modify `src/crypto/config/tasks.yaml` to define your tasks
- Modify `src/crypto/crew.py` to add your own logic, tools and specific args
- Modify `src/crypto/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry run crypto
```

This command initializes the crypto Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The crypto Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Getting Help

If you encounter any issues or have questions, there are several ways to get help:
- Visit our [documentation](https://docs.crewai.com) for detailed guides and API references.
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai) by opening an issue.
- Join our community on [Discord](https://discord.com/invite/X4JWnZnxPb) to connect with other users and developers.
- Chat with our docs using [ChatGPT](https://chatg.pt/DWjSBZn) for quick assistance.

## Support

For support, questions, or feedback regarding the Crypto Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Joing our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat wtih our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.