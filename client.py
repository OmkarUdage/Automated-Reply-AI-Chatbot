# Cohere AI API integration 
import cohere

co = cohere.ClientV2("ryuzsDhsqGoxvlPVyC3eCrzTnpUgubMk2huH09AA")

command = '''
[07:39, 18/07/2025] Shubham Dada: https://www.instagram.com/reel/DMNzpzmJ3t1/?igsh=eDFmdnM1YWo0d2lt
[10:33, 26/07/2025] Shubham Dada: I'm really enjoying this course on Udemy and think you might like it too.
https://www.udemy.com/share/103BPI3@5XRebDvG6UHGqu8yCAv9IEAcj_pGDAfA6yGZea_Zf0vjVjCK0dw5u-WqV8Ny0_U3BQ==/
'''
response = co.chat(
    model="command-a-03-2025", 
    messages=[
        {"role": "system", "content": "You are Omkar, a skilled programmer from India who speaks fluent English but also knows and understand Hindi and Marathi. You reply casually and naturally, like chatting with a friend on WhatsApp. Keep your tone helpful, conversational, and human — avoid sounding robotic or too formal. Output should be the next chat response in short(test message only and not with date and time)"},
        {"role": "user", "content": command}
    ]
)

print(response.message.content[0].text)
