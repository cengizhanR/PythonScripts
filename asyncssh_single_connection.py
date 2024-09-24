import asyncio
import asyncssh

async def connect(host,username,password,command):
    async with asyncssh.connect(host=host,username=username,password=password,known_hosts=None) as connection:
        # result = await connection.run(command)
        # return result
        #2.run multiple commands
        results=[]
        for cmd in command:
            result = await connection.run(cmd)
            results.append(result)

        return results

command = ('ifconfig','who -a','uname -a',)
results2 = asyncio.run(connect('192.168.56.2','ubuntunode01','123',command))
for result in results2:
    print(f'STDOUT:\n{result.stdout}')
    print(f'STDEER:\n{result.stderr}')
    print('#'*50)