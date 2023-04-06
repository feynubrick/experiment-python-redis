import json
import redis


class RedisClient:
    def __init__(self) -> None:
        self._pool = redis.ConnectionPool(host="localhost", port=6379, db=0)
        self._conn = redis.Redis(connection_pool=self._pool)

    def _set(self, key, value):
        return self._conn.set(str(key), value)

    def _get(self, key):
        return self._conn.get(str(key))

    def set(self, key, value):
        return self._set(key, json.dumps(value))

    def get(self, key):
        val = self._get(key)
        if not val:
            return None
        return json.loads(val.decode())

    def _delete(self, key):
        return self._conn.delete(str(key))

    def delete(self, key):
        return self._delete(key)

redis_client = RedisClient()
