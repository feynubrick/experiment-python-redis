from redis_manager import redis_client

if __name__ == "__main__":
    print(redis_client.delete("test"))
    print(redis_client.get("test"))
    print(redis_client.set("test", {"a": 0, "b": 1}))
    print(redis_client.get("test"))
    print(redis_client.delete("test"))
    print(redis_client.get("test"))
