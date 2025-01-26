from src.greate import greate


def test_greate_alice_return_hello_alice():
    assert greate("Alice") == "Hello, Alice"


def test_greate_ossama_return_hello_ossama():
    assert greate("Ossama") == "Hello, Ossama"
