import dotenv


class CredentialService:
    def __init__(self) -> None:
        self.env = dotenv.dotenv_values()

    def get_env_key(self, key) -> str | None:
        return self.env.get(key)
