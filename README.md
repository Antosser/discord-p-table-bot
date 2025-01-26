# Discord Periodic Table Bot

This project is a Discord bot that analyzes user messages to determine if they can be represented using symbols from the periodic table of elements. If a message qualifies, the bot responds with the decomposition of the message into periodic table symbols.

![image](https://github.com/user-attachments/assets/cbd9ff04-2b0f-4072-9c11-e0b3c77d18e3)


## Features

- Responds to messages in Discord channels.
- Checks if a message can be represented entirely using periodic table symbols.
- Sends a congratulatory message with the decomposition of the message if successful.
- Logs the decomposition to the console for debugging and verification.

## Requirements

- Python 3.8+
- A Discord account and bot token.
- Required Python libraries (see `requirements.txt`).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/discord-p-table-bot.git
   cd discord-p-table-bot
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your bot token:

   ```env
   TOKEN=your_discord_bot_token
   ```

5. Make sure the required intents are enabled for your bot in the Discord Developer Portal:
   - Navigate to the **Bot** section of your application settings.
   - Enable the **MESSAGE CONTENT INTENT**.

## Usage

1. Run the bot:

   ```bash
   python main.py
   ```

2. Invite the bot to your Discord server using the OAuth2 URL generated in the Discord Developer Portal.

3. In any text channel where the bot has access, send a message. If the message can be represented with periodic table symbols, the bot will respond with the decomposition.

## File Structure

- `main.py`: The main bot script.
- `ptable.py`: Contains the `decompose_into_symbols` function to break a message into periodic table symbols.
- `.env`: File for storing the bot token (not included in the repository for security).
- `requirements.txt`: List of Python dependencies.
- `Dockerfile`: Configuration for containerizing the bot.
- `compose.yml`: Docker Compose file for running the bot.

## Example

Message:

```
Neon
```

Bot Response:

```
Congratulations! Your message can be written only using symbols from the periodic table! (`Ne`, `O`, `N`)
```

Console Log:

```
Decomposed message: Neon -> ['Ne', 'O', 'N']
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
