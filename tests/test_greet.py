from hello.greet import hello


def test_greet(default_greeting):
    """Check that we can greet the world"""
    assert hello(default_greeting) == "Hello, World!"
