import voltage  # Import voltage.
from voltage.ext import commands  # Importing the commands framework so we that we're able to create a Cog object.


# Next up is the setup function, aka where all the magic happens.
# This is what's actually called by the client to be used for `add_cog`.
# Here you define your cog, define it's commands then return the cog so that the client is able to add it.
# Additionally, any args / kwargs you pass to the `client.add_extension` function will be passed to the setup function.
# The client is passed by default however.
def setup(client) -> commands.Cog:

    test = commands.Cog( # Create a new Cog object.
        "Test", # Give it a name.
        "Some commands for testing." # And an optional description.
    )  # The name and description will be used in the help command.

    # Register a command as normal, difference is you use the Cog object instead of the client in the decorator.
    @test.command()
    async def ping(ctx): # No self parameter.
        """Sends Pong!"""
        await ctx.reply("Pong from inside a Cog!")

    return test # Finally, return the cog object.

# To load a Cog to the client you run `client.add_extension(path, *args, **kwargs)` with the path being the Python dotpath to your file, args and kwargs are optional.

