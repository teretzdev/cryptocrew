# API Reference for Crypto Crew

This document provides a comprehensive reference for the public APIs available in the Crypto Crew project. It includes details about the main classes, methods, and functions, along with examples of how to use them.

## Overview

The Crypto Crew project is designed to facilitate the creation and management of AI agents that perform tasks related to cryptocurrency analysis and reporting. The primary components of the API include the `CryptoCrew` class, the `MyCryptoTool` class, and the `run` function.

## CryptoCrew Class

The `CryptoCrew` class is the core component of the project, responsible for managing agents and tasks.

### Initialization

```python
from crypto.crew import CryptoCrew

crew = CryptoCrew()
```

### Methods

- **portfolio_manager**: Initializes the portfolio manager agent.
  - **Returns**: An `Agent` object configured for managing the portfolio.

- **reporting_analyst**: Initializes the reporting analyst agent.
  - **Returns**: An `Agent` object configured for creating reports.

- **get_highest_position_in_portfolio_task**: Defines a task to find the highest position in the portfolio.
  - **Returns**: A `Task` object for the highest position task.

- **reporting_task**: Defines a task for generating reports.
  - **Returns**: A `Task` object for the reporting task.

- **crew**: Creates and returns a `Crew` object that manages the execution of tasks.
  - **Returns**: A `Crew` object.

### Example Usage

```python
crew = CryptoCrew()
crew.crew().kickoff()
```

## MyCryptoTool Class

The `MyCryptoTool` class is a custom tool used by the portfolio manager to determine the asset with the highest value in the portfolio.

### Methods

- **_run**: Executes the tool's logic to find the highest value asset.
  - **Returns**: A string representing the ticker symbol of the asset with the highest value.

### Example Usage

```python
from crypto.tools.custom_tool import MyCryptoTool

tool = MyCryptoTool()
highest_value_asset = tool._run()
print(highest_value_asset)
```

## run Function

The `run` function is the main entry point for executing the Crypto Crew project.

### Example Usage

```python
from crypto.main import run

run()
```

This function initializes the `CryptoCrew` and starts the execution of tasks as defined in the configuration files.

## Conclusion

This API reference provides an overview of the main components of the Crypto Crew project. For more detailed information on configuration and usage, refer to the project's documentation and configuration files.
