import asyncio
import shlex
from typing import Tuple

import config
from ..logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    """
    Git disabled for Docker/Railway deploys.
    Prevents Bad git executable errors.
    """
    LOGGER(__name__).info("Git sync disabled (running in container environment).")
    LOGGER(__name__).info("Skipping repository fetch/update steps.")

    # Still install requirements (optional)
    try:
        install_req("pip3 install --no-cache-dir -r requirements.txt")
    except Exception:
        pass

    return True
