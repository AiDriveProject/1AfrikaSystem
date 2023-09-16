class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox_button'),
            chatBox: document.querySelector('.chatbox_support'),
            sendButton: document.querySelector('.send_button')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // show or hides the box
        if(this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    async sleep(ms){
        return new Promise(resolve => setTimeout(resolve,ms))
    }

    async onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }
        console.log('Sending message...');

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);
        this.updateChatText(chatbox);

        await this.sleep(3000);

        fetch('http://127.0.0.1:5000/api/endpoint', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          .then(data => {
            let msg2 = { name: "AIDrive", message: data.botResponse };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''

        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "AIDrive")
            {
                html += '<div class="messages_item messages_item--visitor">' + item.message + '</div>'
            }
            else
            {
                html += '<div class="messages_item messages_item--operator">' + item.message + '</div>'
            }
          });

        const chatmessage = chatbox.querySelector('.chatbox_messages');
        chatmessage.innerHTML = html;
    }
}
const chatbox = new Chatbox();
chatbox.display();