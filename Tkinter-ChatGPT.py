import openai
import tkinter as tk

openai.api_key = ""

class ChatBotWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GPT Assistant")
        
        # OpenAI API Credentials Parse
        self.api_key_label = tk.Label(text="OpenAI API Key:")
        self.api_key_label.pack()
        self.api_key_input = tk.Entry()
        self.api_key_input.insert(0, openai.api_key)
        self.api_key_input.pack()

        self.apply_button = tk.Button(text="Apply", command=self.apply_api_key)
        self.apply_button.pack()
        
        # Chat History
        self.message_input = tk.Entry(width=80)
        self.message_input.pack()
        self.message_input.bind("<Return>", self.send_message)
        self.send_button = tk.Button(text="Send", command=self.send_message)
        self.send_button.pack()
        
        
        self.chat_history = tk.Text(height=20, width=50, stat="disabled")
        self.chat_history.pack()
        
        
        # Clear Chat History
        self.clear_button = tk.Button(text="Clear", command=self.clear_history)
        self.clear_button.pack()
        
        # Set Chat Messages
        self.messages = []
        self.window.mainloop()
        
    def apply_api_key(self):
        # Apply OpenAI API Key
        openai.api_key = self.api_key_input.get()
        
    def send_message(self, event=None):
        # Send Message to OpenAI API and display response in chat history
        prompt = self.message_input.get()
        message_user = {"role": "user", "content": prompt}
        self.messages.append(message_user)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,                
            max_tokens=1024,
            temperature=0
        )
            
        message_GPT = {"role": "assistant", "content": response.choices[0].message.content}
        self.messages.append(message_GPT)
            
        self.chat_history.configure(state="normal")
        self.chat_history.insert(tk.END, f"\n\nYou: {prompt}\n\nAssistant: {response.choices[0].message.content}")
        self.chat_history.configure(state="disabled")
            
        self.message_input.delete(0, tk.END)
            
            
    def clear_history(self):
        # Clear Chat History
        self.chat_history.configure(state="normal")
        self.chat_history.delete(1.0, tk.END)
        self.chat_history.configure(state="disabled")
        self.messages = []
            
if __name__ == "__main__":
    chatbot_window = ChatBotWindow()    
