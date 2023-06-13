import revolt
from revolt.ext import commands
from utility.logger import *
import pathlib


class Zorak(commands.CommandsClient):
    async def get_prefix(self, message: revolt.Message):
        return "/"

    async def on_ready(self):
        log_info(f"{self.user.name} is ready to destroy the planet.")
        await self.edit_status(presence=revolt.PresenceType.online, text="I'm watching you.")

    def load_extensions(self):
        zorak_path = pathlib.Path.cwd() / "zorak"
        cogs = zorak_path / "cogs"

        for path in cogs.iterdir():
            log_info(path)
            if path.stem.startswith("_") or path.suffix != ".py":
                continue
            log_info(f'loading cog: {path}')
            self.load_extension(f"Zorak-Revolt.cogs.{path.stem}")

