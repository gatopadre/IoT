from helpers.color import TerminalColors


def show_message(message_type, message_text):
    if message_type == 'bold':
        print(TerminalColors.BOLD + '[ATENTION]:\t {}'.format(message_text) + TerminalColors.CLEAR)
    elif message_type == 'debug':
        print(TerminalColors.DEBUG + '[DEBUG   ]:\t {}'.format(message_text) + TerminalColors.CLEAR)
    elif message_type == 'error':
        print(TerminalColors.FAIL + '[ERROR   ]:\t {}'.format(message_text) + TerminalColors.CLEAR)
    elif message_type == 'info':
        print(TerminalColors.INFO + '[INFO    ]:\t {}'.format(message_text) + TerminalColors.CLEAR)
    elif message_type == 'success':
        print(TerminalColors.SUCCESS + '[SUCCESS ]:\t {}'.format(message_text) + TerminalColors.CLEAR)
    elif message_type == 'warning':
        print(TerminalColors.WARNING + '[WARNING ]:\t {}'.format(message_text) + TerminalColors.CLEAR)
    else:
        print(TerminalColors.UNDERLINE + '[UKNOW]:\t {}'.format(message_text) + TerminalColors.CLEAR)