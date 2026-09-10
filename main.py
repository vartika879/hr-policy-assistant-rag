from hr_assistant.pipeline import ask,build_hr_assistant

def main():
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

if __name__ == "__main__":
  main()