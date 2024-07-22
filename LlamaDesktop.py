from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from openai import OpenAI


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.apiKey=#YOUR API GOES HERE

        # Set up the layout
        self.layout = QVBoxLayout()

        # Create a label for display
        self.label = QLabel('Ask me anything', self)
        self.label.setStyleSheet("font-size: 20px;") 
        self.layout.addWidget(self.label)

        # Create an input field
        self.input_field = QLineEdit(self)
        self.layout.addWidget(self.input_field)

        # Create a button
        self.button = QPushButton('Send the message', self)
        self.button.clicked.connect(self.update_display)
        self.layout.addWidget(self.button)

        # Set the layout for the window
        self.setLayout(self.layout)
        self.setWindowTitle('PyQt5 Llama')

        self.resize(800, 600)

    def update_display(self):
        # Get text from input field and set it to label
        input_text = self.input_field.text()
        self.client = OpenAI(
            api_key = self.apiKey,
            base_url = "https://api.llama-api.com"
            )
        self.response = self.client.chat.completions.create(
            model="llama-70b-chat",
            messages=[
                {"role": "user", "content": input_text}
                ],
                max_tokens=2048)
        self.label.setText(self.response.choices[0].message.content)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
