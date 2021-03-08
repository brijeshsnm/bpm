import asyncio
from TCPServer import TCPServer
import config as cfg


async def main(host, port):
    server = TCPServer()
    server = await asyncio.start_server(server.start_server, host, port)
    await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main(cfg.host['server'], cfg.host['port']))
