from redis_manager import redis_client

if __name__ == "__main__":
    redis_client.set("test", "wow")
    print(redis_client.get("test"))
