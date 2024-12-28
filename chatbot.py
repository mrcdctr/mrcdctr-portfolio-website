from transformers import pipeline

chatbot = pipeline('text-generation', model='gpt2')

while True:
    prompt = input("You: ")
    if prompt.lower() in ["exit", "quit"]:
        break
    response = chatbot(prompt, max_length=50, num_return_sequences=1)
    print("Bot:", response[0]['generated_text'])
