import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Kalshi Configuration
KALSHI_API_KEY = os.getenv("KALSHI_API_KEY")
KALSHI_PRIVATE_KEY_PATH = os.getenv("KALSHI_PRIVATE_KEY_PATH", "kalshi_private.key")
KALSHI_BASE_URL = os.getenv("KALSHI_BASE_URL", "https://api.kalshi.com/v1")

# Polymarket Configuration
POLYMARKET_API_KEY = os.getenv("POLYMARKET_API_KEY")
POLYMARKET_API_SECRET = os.getenv("POLYMARKET_API_SECRET")
POLYMARKET_PASSPHRASE = os.getenv("POLYMARKET_PASSPHRASE")
POLYMARKET_BASE_URL = os.getenv("POLYMARKET_BASE_URL", "https://clob.polymarket.com")

# Environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Validate required keys
def validate_config():
    required = [
        ("KALSHI_API_KEY", KALSHI_API_KEY),
        ("KALSHI_PRIVATE_KEY_PATH", KALSHI_PRIVATE_KEY_PATH),
        ("POLYMARKET_API_KEY", POLYMARKET_API_KEY),
        ("POLYMARKET_API_SECRET", POLYMARKET_API_SECRET),
        ("POLYMARKET_PASSPHRASE", POLYMARKET_PASSPHRASE),
    ]
    
    missing = [name for name, value in required if not value]
    
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
    
    # Check if private key file exists
    if not Path(KALSHI_PRIVATE_KEY_PATH).exists():
        raise ValueError(f"Kalshi private key file not found: {KALSHI_PRIVATE_KEY_PATH}")
    
    return True