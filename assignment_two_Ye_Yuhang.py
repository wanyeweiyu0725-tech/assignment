# Assignment 2: QA Bot
print("Question Answering Bot")

question = input("Ask me something(HKU/robot/jetson/ai/human):")

if question == "HKU":
    print("Bot: HKU stands for The University of Hong Kong.")
elif question == "robot":
    print("Bot: Robots are programmable machines that can execute tasks.")
elif question == "jetson":
    print("Bot: Jetson Nano is an AI computer designed for embedded systems.")
elif question == "ai":
    print("Bot: AI means Artificial Intelligence.")
elif question == "human":
    print("Bot: Humans are intelligent, biological beings.")
else:
    print("Bot: Sorry, I don't understand.")
