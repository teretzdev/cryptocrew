# Configuration Documentation

This document provides detailed information on configuring the agents and tasks in the Crypto Crew project. The configuration is managed through two primary YAML files: `agents.yaml` and `tasks.yaml`. Understanding and customizing these files allows you to tailor the behavior of the AI agents and tasks to suit your specific needs.

## Agents Configuration

The `agents.yaml` file defines the agents used in the project. Each agent has specific settings that determine its role, goals, and behavior.

### Structure of `agents.yaml`

```yaml
portfolio_manager:
  role: "Senior Portfolio Manager"
  goal: "You Manage the Portfolio and give information about the assets in the portfolio"
  backstory: "You're a seasoned portfolio manager. You can provide information about the last transactions and the positions in the portfolio. You answer only with the ticker symbol of the assets. For example, if the last transaction was with bitcoin, you answer BTC."

reporting_analyst:
  role: "Crypto Reporting Analyst"
  goal: "Create detailed reports based on a given ticker symbol of an asset"
  backstory: "You're a professional analyst with a keen eye for detail. You can get a ticker symbol and find useful information on the internet about the given ticker symbol. You can create clear and concise reports, making it easy for others to understand and act on the information you provide. You provide your information always in markdown format. If needed, you use markdown tables."
```

### Customizing Agents

- **Role**: Define the primary function of the agent. For example, a "Market Analyst" could be added to analyze market trends.
- **Goal**: Specify what the agent aims to achieve. Adjust this to align with your project objectives.
- **Backstory**: Provide context or background for the agent. This can be useful for understanding the agent's perspective and behavior.

#### Example Customization

To add a new agent for risk assessment:

```yaml
risk_assessor:
  role: "Risk Assessment Specialist"
  goal: "Evaluate the risk associated with different assets in the portfolio"
  backstory: "With years of experience in financial risk management, you provide insights into potential risks and suggest mitigation strategies."
```

## Tasks Configuration

The `tasks.yaml` file defines the tasks that agents will perform. Each task has specific settings that determine its description and expected output.

### Structure of `tasks.yaml`

```yaml
highest_position_task:
  description: "Find the ticker symbol of the asset with the highest value in the private portfolio. Do only use provided tools as this information is private and not on Internet or in the training data."
  expected_output: "Json formatted answer like {\"highest_ticker_symbol\":\"BTC\"} or if there was no transaction {\"highest_ticker_symbol\":\"No Transaction\"}."

reporting_task:
  description: "You will be provided with a ticker symbol. Make a thorough research about that given ticker symbol. Make sure you find recent and relevant information about the given ticker symbol. Review the context you got make a report in markdown. If possible use a markdown table with source and news."
  expected_output: "A fully fledged report about a ticker symbol in markdown table format. Formatted as markdown without '```'."
```

### Customizing Tasks

- **Description**: Clearly define what the task entails. Modify this to suit the specific actions you want the agent to perform.
- **Expected Output**: Specify the format and type of output expected from the task. Ensure this aligns with your data processing needs.

#### Example Customization

To add a new task for sentiment analysis:

```yaml
sentiment_analysis_task:
  description: "Analyze the sentiment of recent news articles related to a given ticker symbol."
  expected_output: "A sentiment score and summary of the analysis in markdown format."
```

## Customization Guidance

- **Align with Objectives**: Ensure that the roles, goals, and tasks align with your project's objectives.
- **Iterative Testing**: Test configurations iteratively to refine agent behaviors and task outputs.
- **Documentation**: Keep detailed documentation of changes to configurations for future reference and troubleshooting.

By customizing the `agents.yaml` and `tasks.yaml` files, you can effectively tailor the Crypto Crew project to meet your specific requirements and achieve your desired outcomes.
