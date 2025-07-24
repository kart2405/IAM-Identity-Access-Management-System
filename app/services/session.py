import redis
from app.config import settings


redis_client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)


class SessionService:
    @staticmethod
    def store_token(jti: str, user_id: int, expires_in: int):
        redis_client.setex(f"token:{jti}", expires_in, user_id)

    @staticmethod
    def revoke_token(jti: str):
        redis_client.set(f"revoked:{jti}", 1)

    @staticmethod
    def is_token_revoked(jti: str) -> bool:
        return redis_client.exists(f"revoked:{jti}") == 1 