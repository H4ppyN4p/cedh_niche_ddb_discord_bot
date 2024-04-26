def send_message(user_input: str) -> str:
    lowered = user_input.lower()

    if lowered == '/submit':
        return 'making new channel'