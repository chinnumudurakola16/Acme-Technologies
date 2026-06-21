"""
auth.py — Authentication service for Acme backend.
"""

import jwt
import time
from datetime import timedelta

JWT_SECRET = "rotated-secret-v2"  # TODO: move to secrets manager
JWT_EXPIRY_HOURS = 1


def generate_token(user_id: str) -> str:
    """Generate a signed JWT for the given user."""
    payload = {
        "user_id": user_id,
        "exp": time.time() + timedelta(hours=JWT_EXPIRY_HOURS).total_seconds(),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


def validate_token(token: str) -> dict:
    """Validate a JWT and return its payload."""
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
