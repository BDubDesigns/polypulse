# PolyPulse

PolyPulse is a Discord bot built with Python and discord.py that interacts with the Polymarket API for portfolio tracking, trading, stop loss management, and more.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/BDubDesigns/polypulse.git
   cd polypulse
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up configuration:
   - Copy `config.py.example` to `config.py`
   - Replace `YOUR_DISCORD_BOT_TOKEN` in `config.py` with your actual Discord bot token
   - You can get a token from the [Discord Developer Portal](https://discord.com/developers/applications)

4. Run the bot:
   ```bash
   python polypulse/main.py
   ```

## Features
- Portfolio management
- Market data monitoring
- Trading (market & limit orders)
- Stop loss orders
- Market scouting with scalping calculations

## Contributing
Contributions are welcome! Please ensure you don't commit any sensitive data (tokens, keys, etc).
