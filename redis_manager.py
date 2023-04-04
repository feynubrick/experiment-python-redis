import redis


class RedisClient:
    def __init__(self) -> None:
        self._pool = redis.ConnectionPool(host="localhost", port=6379, db=0)
        self._conn = redis.Redis(connection_pool=self._pool)

    def set(self, key, value):
        return self._conn.set(key, value)

    def get(self, key):
        return self._conn.get(key)

redis_client = RedisClient()
