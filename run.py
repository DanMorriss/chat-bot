import openai, os

openai.api_key = os.environ.get('SECRET_KEY')

def chat_with_gpt(prompt, conversation=[]):
    conversation = []

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    conversation = []
    print("Chatbot: Hi there! How can I assist you today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['quit', 'exit', 'bye']:
            break

        response = chat_with_gpt(user_input, conversation)
        print("Chatbot: ", response)
        conversation.append({"role": "assistant", "content": response})
