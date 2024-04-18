import asyncio
import time
import re
from datetime import datetime
import pytz
from dotenv import load_dotenv, find_dotenv

def current_time(firstArg=0):
    time=datetime.now(tz=pytz.UTC)
    return time

async def timer(firstArg):
    delay = re.findall(r'\d+', firstArg)
    delay = int(delay[0])
    reason = re.sub(r'\d+', '', firstArg)
    await asyncio.sleep(delay)
    return (f"Timer for{reason} has ended.")

async def set_timer(firstArg):
    res = await timer(firstArg)
    return res
    

if __name__ == '__main__':
    print(asyncio.run(set_timer("1 to wash clothes")))