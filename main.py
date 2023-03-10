import asyncio
from datetime import datetime as dt

################
# Start locally via:
# python -m http.server 3000
# http://localhost:3000/
################


def format_date(dt_, fmt="%m/%d/%Y, %H:%M:%S"):
    return f"{dt_:{fmt}}"

def now(fmt="%m/%d/%Y, %H:%M:%S"):
    return format_date(dt.now(), fmt)

async def foo():
    while True:
        await asyncio.sleep(1)
        output = now()
        Element("outputDiv2").write(output)

        out3 = Element("outputDiv3")
        if output[-1] in ["0", "4", "8"]:
            out3.write("It's espresso time!")
        else:
            out3.clear()

pyscript.run_until_complete(foo())

