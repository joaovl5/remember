import dotenv

env = dotenv.dotenv_values()


def get_env_key(key) -> str | None:
    return env.get(key)
