from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        # Assistant messages store previous assistant responses, but can also be written by you to give examples of desired behavior.
        {
            "role": "assistant",
            "content": "The Los Angeles Dodgers won the World Series in 2020.",
        },
        {"role": "user", "content": "Where was it played?"},
    ],
)

print(response.choices[0].message)

"""
response.json() shows this:

{
    "id": "chatcmpl-91I4XlAJ4XvzxCFmi5dBXZzlTXOWU",
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": null,
            "message": {
                "content": "The 2020 World Series was played at Globe Life Field in Arlington, Texas.",
                "role": "assistant",
                "function_call": null,
                "tool_calls": null
            }
        }
    ],
    "created": 1710094825,
    "model": "gpt-3.5-turbo-0125",
    "object": "chat.completion",
    "system_fingerprint": "fp_4f0b692a78",
    "usage": {
        "completion_tokens": 17,
        "prompt_tokens": 53,
        "total_tokens": 70
    }
}

"""
