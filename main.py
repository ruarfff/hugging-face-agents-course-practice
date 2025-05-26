from huggingface_hub import InferenceClient


def main():
    print("Hello from hugging-face-agents-course-practice!")

    client = InferenceClient("meta-llama/Llama-3.3-70B-Instruct")
    messages = [
        {"role": "user", "content": "The capital of France is"}
    ]
    output = client.chat_completion(
        messages=messages,
        max_tokens=100,
    )

    print(output.choices[0].message.content)


if __name__ == "__main__":
    main()
