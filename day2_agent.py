class MemoryAgent:
    def __init__(self):
        self.memory = {}

    def store(self, key, value):
        self.memory[key] = value

    def recall(self, key):
        return self.memory.get(key, "No memory found.")


class BusinessTextHelperAgent:
    def __init__(self):
        self.memory = MemoryAgent()

    def summarize_text(self, text):
        sentences = [s.strip() for s in text.split(".") if s.strip()]
        if len(sentences) == 0:
            return "No meaningful text found to summarize."
        if len(sentences) == 1:
            return sentences[0]
        return sentences[0] + ". " + sentences[-1] + "."

    def rewrite_professionally(self, text):
        return f"Professionally rewritten version: {text.strip().capitalize()}."

    def convert_to_bullets(self, text):
        parts = [part.strip() for part in text.split(",") if part.strip()]
        if not parts:
            return "No content found to convert into bullet points."
        return "\n".join([f"- {part}" for part in parts])

    def respond(self, user_input):
        cleaned_input = user_input.strip()
        lower_input = cleaned_input.lower()

        if lower_input == "last task":
            return self.memory.recall("last_task")

        if lower_input.startswith("summarize:"):
            text = cleaned_input[len("summarize:"):].strip()
            self.memory.store("last_task", "summarize")
            self.memory.store("last_text", text)
            return self.summarize_text(text)

        elif lower_input.startswith("rewrite:"):
            text = cleaned_input[len("rewrite:"):].strip()
            self.memory.store("last_task", "rewrite")
            self.memory.store("last_text", text)
            return self.rewrite_professionally(text)

        elif lower_input.startswith("bullets:"):
            text = cleaned_input[len("bullets:"):].strip()
            self.memory.store("last_task", "bullets")
            self.memory.store("last_text", text)
            return self.convert_to_bullets(text)

        else:
            return (
                "I am still learning. Use one of these formats:\n"
                "summarize: your text\n"
                "rewrite: your text\n"
                "bullets: your text\n"
                "Type 'last task' to recall the previous action."
            )


if __name__ == "__main__":
    agent = BusinessTextHelperAgent()

    print("Business Text Helper Agent is running. Type 'exit' to stop.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower().strip() == "exit":
            print("Goodbye!")
            break

        response = agent.respond(user_input)
        print("\nAgent:")
        print(response)