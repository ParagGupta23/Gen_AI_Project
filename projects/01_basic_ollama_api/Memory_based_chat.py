from openai import OpenAI
client = OpenAI(
    base_url = "http://localhost:11434/v1",
    api_key= "ollama"
)
system_prompt = input("Enter system prompt: ")
user_prompt = input("Enter user prompt: ")

messages =[{"role": "system","content":system_prompt}]
while True:
    user_input =input("\nYou: ")
    if user_input.lower() in ["exit","quit"]:
        break
    messages.append({"role":"user","content":user_input})
    response =client.chat.completions.create(
        model ="llama3.2:1b",
        messages =messages
    )
    reply =response.choices[0].message.content
    print("\nAI:",reply)
    messages.append({"role":"assistant","content":reply})
