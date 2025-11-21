import os

import aiofiles

from .enums import Path


class FileManager:

    @staticmethod
    async def read(*args, **kwargs):
        args = [arg.value if isinstance(arg, Path) else str(arg) for arg in args]
        path = os.path.join(*args) + '.txt'
        async with aiofiles.open(path, 'r', encoding='UTF-8') as file:
            response = await file.read()
        return response.strip().format(**kwargs)
