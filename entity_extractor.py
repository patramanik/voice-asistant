def extract_entity(command, intent):
    keywords = {
        "OPEN_APP": ["open", "launch", "start", "run"],
        "PLAY_MUSIC": ["play"],
        "SEARCH_WEB": ["search", "google", "find"]
    }

    if intent in keywords:
        for word in keywords[intent]:
            command = command.replace(word, "")
        return command.strip()

    return command
