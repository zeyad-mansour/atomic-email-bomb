# Atomic-Email-Bomb 💥

This is a tool for flooding an email address with many emails.

## Disclaimer
Neither creator may be held liable for any consequence of this tool's usage. Please note that this is all for fun and games and should not be used for malicious purposes. Using email bombers for harassment or denial-of-service attacks is unethical and illegal; we do not condone that in any way.

## Installation

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary dependencies.
```
pip3 install -r requirements.txt
```
2. Update the [accounts.txt](/bomber/accounts.txt) file with Gmail account(s) that have NFA and enabled access to less secure apps following the defined format.

## Usage
Arguments must be passed by running the program via the CLI. For example,
```
python3 bomb.py recieving_email@domain.com 500 "subject" "body"
```
The last two arguments are not necessary; if they are not included, the subject and body will auto-generate. If one of the two is included, the other must be also.

## Notes
1. By default, Gmail accounts have a sending limit of 500 emails per day. Gmail Workspace (formerly G Suite) accounts have a sending limit of 2000 emails per day.
2. If Gmail detects the email bomber, sending from that account may be temporarily paused; use at your own risk.

## Future Updates
1. Temporarily remove blocked or paused accounts from the list during random sending
2. Implement multithreading so that emails can be sent at a greater rate

## License
[MIT](https://github.com/zeyad-mansour/atomic-email-bomb/blob/main/LICENSE)
