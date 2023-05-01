# MORE ON STRINGS: multi-line strings, <class 'str'>.methods(), escape sequences, 
print('(START)')
username = "lannister_one"
client_name = "Jamie Lannister"
brand_name = "Game of Thrones Corporation"
dept_chair = "George R.R. Martin"
loc = "New York, NY 10001, USA"

message = """
Hello {client}({username}),

Thank you for signing up for {co}. We are excited to have you as one of unique members.

Here is your membership information: ...
Here is your locker combination: .... 
Please change your locker PIN at each visit.

Please give us a call back at 9179179179 should you have any questions.

Best regards,\n{manager}\n{co}\n{loc}
""".format(client=client_name, username=username, co=brand_name, manager=dept_chair, loc=loc, )

user_inbox = [message]
print("\nEXAMPLE 1: Using <class str>.format() to create and format new strings:")
print(f"inbox({len(user_inbox)}")
# a function to showMessagesFrom(user_inbox)
current_msg_index = 0
print("message:", user_inbox[current_msg_index])
print('(END)')
