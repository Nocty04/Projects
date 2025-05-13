from lines import line_count
import pytest
import sys

with open("hello.py", "w") as file:
     file.write("Hello\ni am\n super cool")


def test_valid(monkeypatch):
     monkeypatch.setattr(sys, 'argv', ["lines.py", "hello.py"])
     assert line_count() == 3



def test_noexist_or_invalidextension(monkeypatch):
     monkeypatch.setattr(sys, 'argv', ["lines.py", "noexist.txt"])
     with pytest.raises(SystemExit):
          line_count()


def test_too_long(monkeypatch):
     monkeypatch.setattr(sys, 'argv', ["lines.py", "hello.py", "hello.py"])
     with pytest.raises(SystemExit):
          line_count()

def test_too_small(monkeypatch):
     monkeypatch.setattr(sys, 'argv', ["lines.py"])
     with pytest.raises(SystemExit):
          line_count()






