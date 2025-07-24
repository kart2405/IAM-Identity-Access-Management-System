from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
from collections import defaultdict

RATE_LIMIT = 100
WINDOW = 900  # 15 minutes in seconds

class RateLimiter(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.requests = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        ip = request.client.host
        now = time.time()
        window_start = now - WINDOW
        self.requests[ip] = [t for t in self.requests[ip] if t > window_start]
        if len(self.requests[ip]) >= RATE_LIMIT:
            return Response("Too Many Requests", status_code=429)
        self.requests[ip].append(now)
        response = await call_next(request)
        return response 