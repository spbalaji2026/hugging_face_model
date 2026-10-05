from transformers import pipeline

print("Loading AI model...")

pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

print("AI model loaded!")
print("Type 'exit' to stop.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    messages = [
        {
            "role": "user",
            "content": question
        }
    ]

    result = pipe(
        messages,
        max_new_tokens=100
    )

    answer = result[0]["generated_text"][-1]["content"]

    print("AI:", answer)