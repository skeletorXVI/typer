import typer

from docs_src.asynchronous import tutorial001 as async_mod
from typer.testing import CliRunner

runner = CliRunner()

app = typer.Typer()
app.command()(async_mod.main)


def test_asyncio():
    result = runner.invoke(app)

    assert result.exit_code == 0
    assert "Hello World\n" in result.output
