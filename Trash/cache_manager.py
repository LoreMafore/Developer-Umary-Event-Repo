import redis
import json
import time

# Trying to implement caching layer
# Connection keeps timing out

class CacheManager:
    def __init__(self, host='localhost', port=6379):
        try:
            self.redis_client = redis.Redis(
                host=host,
                port=port,
                decode_responses=True
            )
            # TODO: add connection pool
            # self.redis_client.ping()  # this times out
        except redis.ConnectionError:
            print("Could not connect to Redis")
            self.redis_client = None
    
    def get(self, key):
        """Get value from cache"""
        if self.redis_client is None:
            return None
        
        try:
            value = self.redis_client.get(key)
            if value:
                # TODO: handle different data types
                return json.loads(value)
            return None
        except:
            return None
    
    def set(self, key, value, expiry=3600):
        """Set value in cache with expiry"""
        if self.redis_client is None:
            return False
        
        try:
            # Serialize value
            serialized = json.dumps(value)
            # TODO: is expiry in seconds or milliseconds?
            self.redis_client.setex(key, expiry, serialized)
            return True
        except Exception as e:
            print(f"Error setting cache: {e}")
            return False
    
    def delete(self, key):
        """Delete key from cache"""
        # TODO: implement this
        pass
    
    def clear_all(self):
        """Clear all cache"""
        # TODO: implement with pattern matching
        # self.redis_client.flushdb()  # is this too dangerous?
        pass

# TODO: add decorator for caching function results
# def cache_result(expiry=3600):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             # generate cache key
#             # check cache
#             # if miss, call function and cache result
#             pass
#         return wrapper
#     return decorator

if __name__ == "__main__":
    cache = CacheManager()
    
    # Test caching
    # cache.set('user:1', {'name': 'John', 'email': 'john@example.com'})
    # user = cache.get('user:1')
    # print(user)
