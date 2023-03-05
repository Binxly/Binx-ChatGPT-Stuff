import openai
from PyQt5 import QtWidgets, QtCore, QtGui

openai.api_key = ""

class ChatBotWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("ChatGPT Assistant")
        self.setStyleSheet("background-color: #222222; color: #ffffff;")
        self.layout = QtWidgets.QVBoxLayout()
        self.api_key_label = QtWidgets.QLabel("OpenAI API Key:")
        self.api_key_label.setStyleSheet("color: #ffffff;")
        self.layout.addWidget(self.api_key_label)
        self.api_key_input = QtWidgets.QLineEdit()
        self.api_key_input.setText(openai.api_key)
        self.api_key_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.api_key_input.setStyleSheet("background-color: #333333; color: #ffffff;")
        self.layout.addWidget(self.api_key_input)
        self.apply_button = QtWidgets.QPushButton("Apply")
        self.apply_button.setStyleSheet("background-color: #333333; color: #ffffff;")
        self.apply_button.clicked.connect(self.apply_api_key)
        self.layout.addWidget(self.apply_button)
        self.message_input = QtWidgets.QTextEdit()
        self.message_input.setStyleSheet("background-color: #333333; color: #ffffff;")
        self.layout.addWidget(self.message_input)
        self.message_input.textChanged.connect(self.update_send_button)
        self.send_button = QtWidgets.QPushButton("Send")
        self.send_button.setStyleSheet("background-color: #333333; color: #ffffff;")
        self.send_button.setDisabled(True)
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)
        self.chat_history = QtWidgets.QTextEdit()
        self.chat_history.setStyleSheet("background-color: #333333; color: #ffffff;")
        self.chat_history.setReadOnly(True)
        self.chat_history.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse|QtCore.Qt.TextSelectableByKeyboard)
        self.layout.addWidget(self.chat_history)
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.clear_button.setStyleSheet("background-color: #333333; color: #ffffff;")
        self.clear_button.clicked.connect(self.clear_history)
        self.layout.addWidget(self.clear_button)
        self.messages = []
        self.setLayout(self.layout)

    def clear_history(self):
        self.chat_history.clear()
        self.messages = []

    def apply_api_key(self):
        openai.api_key = self.api_key_input.text()

    def update_send_button(self):
        if self.message_input.toPlainText().strip():
            self.send_button.setEnabled(True)
        else:
            self.send_button.setDisabled(True)

    def send_message(self):
        prompt = self.message_input.toPlainText()
        lines = prompt.split('\n')
        messages = [{"role": "user", "content": line} for line in lines]
        self.messages.extend(messages)
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
        self.chat_history.setReadOnly(True)
        self.chat_history.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse|QtCore.Qt.TextSelectableByKeyboard)
        self.message_input.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    chatbot_window = ChatBotWindow()
    chatbot_window.show()
    app.exec_()
