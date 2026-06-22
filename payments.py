"""
payments.py — Payments API for Acme backend.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/v2/payments")

RATE_LIMIT_PER_MINUTE = 100


@router.post("/initiate")
async def initiate_payment(amount: float, currency: str, customer_id: str):
    """Initiate a new payment transaction."""
    # TODO: add idempotency key handling
    return {"transaction_id": "txn_placeholder", "status": "pending"}


@router.get("/{transaction_id}")
async def get_payment_status(transaction_id: str):
    """Return the status of a payment transaction."""
    return {"transaction_id": transaction_id, "status": "completed"}

async def retry_failed_payment(transaction_id: str):
    """Retry a previously failed payment."""
    result = await payment_gateway.retry(transaction_id)  # payment_gateway is never imported
    return result
