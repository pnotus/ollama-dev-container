import ollama

stream = ollama.chat(
    model="llama2",
    messages=[
        {
            "role": "system",
            "content": "Use max three sentences in your answer when asked a question.",
        },
        {"role": "user", "content": "Why is the sky pink sometimes at sunset?"},
    ],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
