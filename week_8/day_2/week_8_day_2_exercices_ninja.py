# EXERCISE NINJA

class Phone:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
        self.outgoing = []
        self.incoming = []
        self.from_which = []

    def call(self, other_phone):
        calling = input(f"From which number is the call, {self.phone_number} (write \'self\') or {other_phone.phone_number} (write \'other\'): ")
        if calling == "self":
            calling = self.phone_number
            called = other_phone.phone_number
        else:
            calling = other_phone.phone_number
            called = self.phone_number
        self.call_history.append(f'{calling} called {called}')

    def show_call_history(self):
        print(self.call_history)

    def send_message(self, other_phone):
        sending = input(f"From which number is the message, {self.phone_number} (write \'self\') or {other_phone.phone_number} (write \'other\'): ")
        if sending == "self":
            sending = self.phone_number
            receiving = other_phone.phone_number
        else:
            sending = other_phone.phone_number
            receiving = self.phone_number
        content = input("What is the message sent: ")
        message = {'to': receiving, 'from': sending, 'content': content}
        self.messages.append(message)

    def show_outgoing_messages(self):
        self.outgoing = [m['content'] for m in self.messages if m['from'] != self.phone_number]
        print(self.outgoing)

    def show_incoming_messages(self):
        self.incoming = [m['content'] for m in self.messages if m['from'] == self.phone_number]
        print(self.incoming)

    def show_messages_from(self):
        from_phone = Phone(input('From which phone number: '))
        self.from_which = [m['content'] for m in self.messages if m['from'] == from_phone.phone_number]
        print(self.from_which)


my_phone = Phone("01 01 01 01")
your_phone = Phone("10 10 10 10")
my_phone.call(your_phone)
print(my_phone.call_history)
my_phone.send_message(your_phone)
print(my_phone.messages)
my_phone.send_message(your_phone)
print(my_phone.messages)
my_phone.send_message(your_phone)
my_phone.show_outgoing_messages()
my_phone.show_incoming_messages()
my_phone.show_messages_from()

