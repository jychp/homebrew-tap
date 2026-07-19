from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("update_elchango_cask.py")
SPEC = importlib.util.spec_from_file_location("update_elchango_cask", MODULE_PATH)
assert SPEC is not None
assert SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RenderCaskTests(unittest.TestCase):
    def test_renders_expected_release_contract(self) -> None:
        rendered = MODULE.render_cask("1.2.3", "a" * 64)

        self.assertIn('version "1.2.3"', rendered)
        self.assertIn(f'sha256 "{"a" * 64}"', rendered)
        self.assertIn(
            "releases/download/v#{version}/"
            "elChango-#{version}-macos-universal.zip",
            rendered,
        )
        self.assertIn("depends_on macos: :sonoma", rendered)
        self.assertIn('app "elChango.app"', rendered)

    def test_rejects_noncanonical_version(self) -> None:
        with self.assertRaisesRegex(ValueError, "strict SemVer"):
            MODULE.render_cask("v1.2.3", "a" * 64)

    def test_rejects_noncanonical_checksum(self) -> None:
        with self.assertRaisesRegex(ValueError, "64 lowercase"):
            MODULE.render_cask("1.2.3", "A" * 64)


if __name__ == "__main__":
    unittest.main()
