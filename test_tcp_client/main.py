import asyncio

async def tcp_echo_client(message, loop):
     reader, writer = await asyncio.open_connection('127.0.0.1', 5000)
     print('Send: %r' % message)
     writer.write(message.encode())

     data = await reader.read(100)
     print('Received: %r' % data.decode())
     print('Close the socket')
     writer.close()

message = '123 BUY 100'
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()