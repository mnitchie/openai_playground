from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        # The system message helps set the behavior of the assistant. For example, you can modify the personality of
        # the assistant or provide specific instructions about how it should behave throughout the conversation.
        # However note that the system message is optional and the model’s behavior without a system message is likely
        # to be similar to using a generic message such as "You are a helpful assistant."
        {
            "role": "system",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
        },
        # The user messages provide requests or comments for the assistant to respond to.
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming.",
        },
    ],
)

print(completion.choices[0].message)
