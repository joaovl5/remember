# Faremos a parte inicial de catalogar os dados do computador e salvá-los em um banco de dados sqlite.
from gui.api import WindowApi
from gui.init import Window
from services.ai_provider import GroqProviderService
from services.credential import CredentialService
import services.logger
import time
import asyncio


async def main():
    creds = CredentialService()
    api = WindowApi(credentials=creds)
    window = Window(api=api)
    window.start()
    # provider = GroqProviderService("llama3-8b-8192")
    # svc = services.logger.LoggerService(provider=provider)
    # while True:
    #     await svc.take_snapshot()
    #     time.sleep(10)


asyncio.run(main())
