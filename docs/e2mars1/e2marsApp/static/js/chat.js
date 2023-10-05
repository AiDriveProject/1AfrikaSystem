class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox_button'),
            chatBox: document.querySelector('.chatbox_support'),
            sendButton: document.querySelector('.send_button')
        }

        this.state = false;
        this.messages = [];
        this.form = document.getElementById('chat-form');
    }

    display() {
        const {openButton, chatBox, sendButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        // Handle form submission
        const form = chatBox.querySelector('#chat-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault(); // Prevent the form from submitting normally

            const text1 = form.querySelector('input[name="message"]').value;

            if (text1 === "") {
                return;
            }

            console.log(text1);
            console.log('Sending message...');

            // Get the CSRF token from the form
            // const csrfToken = form.querySelector('input[name="csrfmiddlewaretoken"]').value;

            let msg1 = { name: "User", message: text1 }
            this.messages.push(msg1);
            this.updateChatText(chatBox);

            await this.sleep(3000);

            fetch('api/endpoint', {
                method: 'POST',
                body: JSON.stringify({ message: text1 }),
                headers: {
                    'Content-Type': 'application/json',
                    //'X-CSRFToken': csrfToken, // Include the CSRF token in the headers
                },
            })
            .then(r => r.json())
            .then(data => {
                let msg2 = { name: "AIDrive", message: data.botResponse };
                this.messages.push(msg2);
                this.updateChatText(chatBox);

                 e.preventDefault();
                 // Display the bot's response in the chatbox
                const chatmessage = chatBox.querySelector('.chatbox_messages');
                chatmessage.innerHTML += '<div class="messages_item messages_item--operator">' + data.botResponse + '</div>';
                form.querySelector('input[name="message"]').value = '';
            })
            .catch((error) => {
                console.error('Error:', error);
                this.updateChatText(chatBox);
                form.querySelector('input[name="message"]').value = '';
            });
        });








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
        console.log(text1);
        console.log('Sending message...');

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);
        this.updateChatText(chatbox);

        await this.sleep(3000);
        //const csrftoken = getCookie('csrftoken');

        fetch('api/endpoint', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            headers: {
              'Content-Type': 'application/json'
              //'X-CSRFToken': csrftoken,
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
