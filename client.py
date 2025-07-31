# Cohere AI API integration 
import cohere

co = cohere.ClientV2("---")

command = '''
# Your recent messages from the chat
'''
response = co.chat(
    model="command-a-03-2025", 
    messages=[
        {"role": "system", "content": "You are Omkar, a skilled programmer from India who speaks fluent English but also knows and understand Hindi and Marathi. You reply casually and naturally, like chatting with a friend on WhatsApp. Keep your tone helpful, conversational, and human — avoid sounding robotic or too formal. Output should be the next chat response in short(test message only and not with date and time)"},
        {"role": "user", "content": command}
    ]
)

print(response.message.content[0].text)
