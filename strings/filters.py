from typing import List, Union

from pyrogram import filters


other_filters = filters.group

def command(commands: Union[str, List[str]]):
    return filters.command(commands, "")
