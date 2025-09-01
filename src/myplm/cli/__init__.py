import click

from myplm.cli.data import data
from myplm.cli.train import train


@click.group(invoke_without_command=True)
@click.version_option()
@click.help_option("--help", "-h")
@click.pass_context
def cli(ctx):
    """Make your own protein language model"""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit(0)


# Attach grouped subcommands
cli.add_command(data)
cli.add_command(train)
