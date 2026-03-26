from openai import OpenAI

client = OpenAI(
    base_url ="http://localhost:11434/v1",
    api_key ="ollama"
)
def summarize_text(text: str)->str:
    prompt = f"""
    Summarize the following content in a clear and {text[ :100]}
    """
    response =client.chat.completions.create(
        model = "llama3.2:1b",
        messages= [
            {"role": "system", "content": "You are a helpful summarization assistant."},
            {"role": "user", "content": prompt}
            ]
    )
    return response.choices[0].message.content