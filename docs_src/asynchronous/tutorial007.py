import asyncio

import typer

app = typer.Typer()


@app.command()
async def wait_trio(seconds: int):
    import trio

    await trio.sleep(seconds)
    typer.echo(f"Waited for {seconds} seconds using trio (default)")


@app.command(async_runner=lambda c: asyncio.run(c))
async def wait_asyncio(seconds: int):
    await asyncio.sleep(seconds)
    typer.echo(f"Waited for {seconds} seconds using asyncio (custom runner)")


if __name__ == "__main__":
    app()