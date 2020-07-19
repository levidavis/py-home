from .config_store import ConfigStore

config = ConfigStore()

config.set_mqtt_broker("mqtt", 1883)

config.set_redis_config("redis", 6379, 0)
