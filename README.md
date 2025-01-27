# Discord Periodic Table Bot

This project is a Discord bot that analyzes user messages to determine if they can be represented using symbols from the periodic table of elements. If a message qualifies, the bot responds with the decomposition of the message into periodic table symbols.

![image](https://github.com/user-attachments/assets/cbd9ff04-2b0f-4072-9c11-e0b3c77d18e3)

## Features

- Responds to messages in Discord channels.
- Checks if a message can be represented entirely using periodic table symbols.
- Sends a congratulatory message with the decomposition of the message if successful.
- Logs the decomposition to the console for debugging and verification.

## Requirements

- Python 3.8+ (for running natively).
- Docker and Docker Compose (for containerized usage).
- A Discord account and bot token.
- Required Python libraries (see `requirements.txt`).

## Installation and Usage

### Option 1: Running Natively

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

5. Enable the **MESSAGE CONTENT INTENT** for your bot in the Discord Developer Portal:
   - Go to the **Bot** section of your application settings.
   - Enable the **MESSAGE CONTENT INTENT**.

6. Run the bot:

   ```bash
   python main.py
   ```

### Option 2: Running with Docker

The bot is also ready to run in a Docker container. Ensure Docker and Docker Compose are installed on your system.

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/discord-p-table-bot.git
   cd discord-p-table-bot
   ```

2. Create a `.env` file in the root directory and add your bot token:

   ```env
   TOKEN=your_discord_bot_token
   ```

3. Start the bot using Docker Compose:

   ```bash
   docker compose up -d
   ```

   This command will:
   - Build the Docker image.
   - Start the bot container in detached mode.

4. To view logs from the running container:

   ```bash
   docker logs -f <container_name>
   ```

   Replace `<container_name>` with the name of the container (e.g., `discord-p-table-bot_main`).

5. To stop the bot:

   ```bash
   docker compose down
   ```

## File Structure

- `main.py`: The main bot script.
- `ptable.py`: Contains the `decompose_into_symbols` function to break a message into periodic table symbols.
- `.env`: File for storing the bot token (not included in the repository for security).
- `requirements.txt`: List of Python dependencies.
- `Dockerfile`: Configuration for building the bot's Docker image.
- `compose.yml`: Docker Compose file for managing the containerized bot.

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
