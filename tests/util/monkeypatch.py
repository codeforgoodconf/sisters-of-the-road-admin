import _pytest.monkeypatch

__all__ = ['MonkeyPatch']


class MonkeyPatch(_pytest.monkeypatch.MonkeyPatch):
    """pytest's MonkeyPatch class, which allows usage as a context manager

    Supports usage in a "with" statement, so undo() needn't be manually called

    Usage:

        with MonkeyPatch() as mp:
            mp.setattr('module.attr', 123)

    """

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.undo()
