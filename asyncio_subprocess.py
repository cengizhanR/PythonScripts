import asyncio

async def run(cmd):
    proc= await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout,stderr=await proc.communicate()
    print(f'{cmd} exited with status code: {proc.returncode}')

    if stdout:
        print(f'Stdout:\n{stdout.decode("UTF-8")}')
    if stderr:
        print(f'Stderr:\n{stderr.decode()}')

async def main(commands):
    task= []
    for cmd in commands:
        task.append(run(cmd))
    await asyncio.gather(*task)

commands=('ipconfig','dir','route dir','arp -a')
asyncio.run(main(commands))

