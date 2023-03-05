import openai
from PyQt5 import QtWidgets

openai.api_key = ""

class ChatBotWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GPT Assistant")
        self.layout = QtWidgets.QVBoxLayout()

        # OpenAI API Credentials Parse
        self.api_key_label = QtWidgets.QLabel("OpenAI API Key:")
        self.layout.addWidget(self.api_key_label)
        self.api_key_input = QtWidgets.QLineEdit()
        self.api_key_input.setText(openai.api_key)
        self.api_key_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.layout.addWidget(self.api_key_input)

        self.apply_button = QtWidgets.QPushButton("Apply")
        self.apply_button.clicked.connect(self.apply_api_key)
        self.layout.addWidget(self.apply_button)

        # Chat History
        self.message_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.message_input)
        self.message_input.returnPressed.connect(self.send_message)
        self.send_button = QtWidgets.QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.chat_history = QtWidgets.QTextEdit()
        self.chat_history.setDisabled(True)
        self.layout.addWidget(self.chat_history)

        # Clear Chat History
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_history)
        self.layout.addWidget(self.clear_button)

        # Set Chat Messages
        self.messages = []
        self.setLayout(self.layout)

    def apply_api_key(self):
        # Apply OpenAI API Key
        openai.api_key = self.api_key_input.text()

    def send_message(self):
        # Send Message to OpenAI API and display response in chat history
        prompt = self.message_input.text()
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

        self.chat_history.setEnabled(True)
        self.chat_history.append(f"\n\nYou: {prompt}\n\nAssistant: {response.choices[0].message.content}")
        self.chat_history.setDisabled(True)

        self.message_input.clear()

    def clear_history(self):
        # Clear Chat History
        self.chat_history.setEnabled(True)
        self.chat_history.clear()
        self.chat_history.setDisabled(True)
        self.messages = []

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    chatbot_window = ChatBotWindow()
    chatbot_window.show()
    app.exec_()
