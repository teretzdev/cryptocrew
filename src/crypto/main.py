from crypto.crew import CryptoCrew


def run():
    try:
        crew = CryptoCrew().crew()
        crew.kickoff()
    except Exception as e:
        print(f"An error occurred during the execution of the CryptoCrew: {e}")