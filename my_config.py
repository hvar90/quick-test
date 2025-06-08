#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os,sys
from contextlib import contextmanager
from typing import Iterator

# 3rd-party
from monkeytype.config import DefaultConfig


class MyConfig(DefaultConfig):
	@contextmanager
	def cli_context(self, command: str) -> Iterator[None]:
		#sys.path.append("/Users/hvar/gitquictest/quicktest")
		os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quicktest")
		import django
		django.setup()
		yield


CONFIG = MyConfig()
