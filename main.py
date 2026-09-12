
"""Command-line demo of the HR Policy Assistant.

Run with:  python main.py
"""
from hr_assistant.pipeline import ask,build_hr_assistant
from hr_assistant.logger import get_logger
logger = get_logger(__name__)
def main():
    logger.info("=== CLI run started ===")
    print(" Buiding the HR Assistant..")

    agent=build_hr_assistant()
    print("ASSISTANT REAdY")

    demo_question=[
        "How many paid leaves days do i get ?",
        "WHAt is the notice period during probation?"
    ]

    for question in demo_question:
        print("="* 60)
        print("QUESTION:",question)
        print("--"*60)
        answer=ask(agent,question)
        print("ANSWER:",answer)
        print("="*60)
        print()
        logger.info("=== CLI run finished ===")

if __name__ == "__main__":
  main()