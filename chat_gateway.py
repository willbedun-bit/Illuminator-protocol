"""
chat_gateway.py

This module connects user input to the Illuminator Protocol engine.
It processes text input, routes it through logic, observer, memory, and ethics,
then returns a filtered, ethically-aligned response.

Author: William Ray Hughes, Jr. (Willbedun)
"""

from core.logic_engine import IlluminatorCore
from core.observer import IlluminatorObserver
from core.ethics_gate import EthicsGate
from core.memory import MemoryManager

class ChatGateway:
    def __init__(self):
        self.engine = IlluminatorCore()
        self.observer = IlluminatorObserver()
        self.ethics = EthicsGate()
        self.memory = MemoryManager()

    def interact(self, user_input):
        """
        Core interaction function: processes input and returns output.
        """
        decision = self.engine.execute(user_input)
        validation = self.ethics.validate(user_input, decision['chosen'])

        if not validation['ethically_approved']:
            response = f"⚠️ Output blocked by Ethics Gate: {validation['violations']}"
        else:
            response = decision['chosen']

        self.observer.observe_interaction(user_input, response)
        self.memory.store({
            "input": user_input,
            "output": response,
            "ethics": validation
        })

        return response

# Optional CLI loop for testing
if __name__ == "__main__":
    chat = ChatGateway()
    print("🧠 Illuminator Chat Gateway — type 'exit' to quit
")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        reply = chat.interact(user_input)
        print(f"AI: {reply}\n")
