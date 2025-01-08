# Environment Variables for Crypto Crew

This document outlines the environment variables required for the Crypto Crew project. These variables are essential for configuring the project and ensuring it operates correctly. Below is a list of the environment variables, their purposes, and instructions on how to obtain the necessary values.

## BINANCE_API_KEY

- **Purpose**: This API key is used to authenticate requests to the Binance API, allowing the project to access account information and market data.
- **How to Obtain**: 
  - Sign up for a Binance account at [Binance](https://www.binance.com/).
  - Navigate to the API Management section in your account settings.
  - Create a new API key and ensure it has the necessary permissions for reading account data and market information.
- **Default Behavior**: There is no default value. This key must be set for the project to interact with Binance.

## BINANCE_SECRET_KEY

- **Purpose**: This secret key is paired with the `BINANCE_API_KEY` to securely sign requests to the Binance API.
- **How to Obtain**: 
  - Follow the same steps as for obtaining the `BINANCE_API_KEY`.
  - The secret key will be provided when you create a new API key in Binance.
- **Default Behavior**: There is no default value. This key must be set for secure communication with Binance.

## OPENAI_API_KEY

- **Purpose**: This API key is used to authenticate requests to OpenAI's API, enabling the project to utilize OpenAI's language models.
- **How to Obtain**: 
  - Sign up for an OpenAI account at [OpenAI](https://www.openai.com/).
  - Access the API section in your account settings to generate a new API key.
- **Default Behavior**: There is no default value. This key must be set for the project to interact with OpenAI's services.

## PAPER_TRADING

- **Purpose**: This variable enables or disables paper trading mode, which allows users to simulate trading without using real funds.
- **How to Set**: 
  - Set this variable to `true` to enable paper trading mode.
  - Set this variable to `false` or leave it unset to disable paper trading mode.
- **Default Behavior**: If not set, the project assumes live trading mode. It is recommended to explicitly set this variable to avoid unintended trading.

## Setting Up Your Environment

To configure your environment, create a `.env` file in the root directory of the project and add the necessary variables with their respective values. You can use the `.env.example` file as a template.

Example `.env` file:

```env
BINANCE_API_KEY=your_binance_api_key
BINANCE_SECRET_KEY=your_binance_secret_key
OPENAI_API_KEY=your_openai_api_key
PAPER_TRADING=true
```

Ensure that your `.env` file is not included in version control to keep your API keys secure.
