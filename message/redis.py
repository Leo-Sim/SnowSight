
import redis

class RedisChannelInfo:

    CHANNEL_INBOUND_TCP = "inbound_tcp"

class RedisClient:
    """
    This class manages redis client and maintains pub/sub pattern
    """
    _client = None

    def __init__(self, host='localhost', port=6379):

        if RedisClient._client is None:
            RedisClient._client = redis.Redis(host=host, port=port)

    @staticmethod
    def get_client():
        return RedisClient._client

    @staticmethod
    def publish(channel, message):
        RedisClient._client.publish(channel, message)

    @staticmethod
    def subscribe(channel):
        pubsub = RedisClient._client.pubsub()
        pubsub.subscribe(channel)
        return pubsub