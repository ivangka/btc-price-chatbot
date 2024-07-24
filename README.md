# BTC Price Chatbot

![GitHub repo size](https://img.shields.io/github/repo-size/ivangka/btc-price-chatbot?style=plastic)

This is a simple Telegram bot built with Python that provides the current Bitcoin price upon user request. The bot fetches the latest Bitcoin price from a public API and sends it to the user in the chat.

## Installation

1. **Clone the repository:**

	```bash
	git clone https://github.com/ivangka/btc-price-chatbot.git
	cd btc-price-chatbot
	```

2. **Create a virtual environment adn activate it:**

	```bash
	python -m venv venv
	source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
	```

3. **Install the required dependencies:**

	```bash
	pip install -r requirements.txt
	```

4. **Set up your Telegram bot:**

	- Create a new bot on Telegram by talking to @BotFather and get the API token.
	- Create a file named config.py in the project directory and add your Telegram bot token:<br>
<br>
	```python
	token_tg = 'your_telegram_bot_token'
	```