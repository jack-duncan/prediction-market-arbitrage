import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Kalshi Configuration
KALSHI_API_KEY = os.getenv("KALSHI_API_KEY")
KALSHI_PRIVATE_KEY_PATH = os.getenv("KALSHI_PRIVATE_KEY_PATH", "kalshi_private.key")
KALSHI_BASE_URL = os.getenv("KALSHI_BASE_URL", "https://api.kalshi.com/v1")

# Polymarket Configuration (py-clob-client SDK)
POLYMARKET_PRIVATE_KEY = os.getenv("POLYMARKET_PRIVATE_KEY")
POLYMARKET_PROXY_ADDRESS = os.getenv("POLYMARKET_PROXY_ADDRESS")
POLYMARKET_BASE_URL = os.getenv("POLYMARKET_BASE_URL", "https://clob.polymarket.com")
POLYMARKET_SIGNATURE_TYPE = int(os.getenv("POLYMARKET_SIGNATURE_TYPE", "1"))
POLYMARKET_CHAIN_ID = int(os.getenv("POLYMARKET_CHAIN_ID", "137"))

# Environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Validate required keys
def validate_config():
    required = [
        ("KALSHI_API_KEY", KALSHI_API_KEY),
        ("KALSHI_PRIVATE_KEY_PATH", KALSHI_PRIVATE_KEY_PATH),
        ("POLYMARKET_PRIVATE_KEY", POLYMARKET_PRIVATE_KEY),
        ("POLYMARKET_PROXY_ADDRESS", POLYMARKET_PROXY_ADDRESS),
    ]
    
    missing = [name for name, value in required if not value]
    
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
    
    # Check if private key file exists
    if not Path(KALSHI_PRIVATE_KEY_PATH).exists():
        raise ValueError(f"Kalshi private key file not found: {KALSHI_PRIVATE_KEY_PATH}")
    
    return True