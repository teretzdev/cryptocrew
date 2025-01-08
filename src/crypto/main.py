"""
Main entry point for the Crypto Crew project.

This module initializes and runs the Crypto Crew, which manages AI agents
and tasks for cryptocurrency analysis and reporting.
"""

from crypto.crew import CryptoCrew


def run():
    """
    Initializes and runs the Crypto Crew.

    This function creates an instance of the CryptoCrew class and starts
    the execution of tasks as defined in the configuration files. It serves
    as the main entry point for the project.
    """
    # Create an instance of CryptoCrew and start the task execution
    CryptoCrew().crew().kickoff()