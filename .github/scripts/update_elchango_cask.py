#!/usr/bin/env python3
"""Generate the elChango Homebrew Cask from a verified release."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

SOURCE_REPOSITORY = "jychp/elchango"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = ROOT / "Casks" / "elchango.rb"


def render_cask(version: str, sha256: str) -> str:
    """Return deterministic Cask source for one elChango release."""
    if not SEMVER.fullmatch(version):
        raise ValueError("version must be strict SemVer in X.Y.Z form")
    if not SHA256.fullmatch(sha256):
        raise ValueError("sha256 must contain 64 lowercase hexadecimal characters")

    return f'''cask "elchango" do
  version "{version}"
  sha256 "{sha256}"

  url "https://github.com/{SOURCE_REPOSITORY}/releases/download/v#{{version}}/elChango-#{{version}}-macos-universal.zip"
  name "elChango"
  desc "Local control deck for native AI coding sessions"
  homepage "https://github.com/{SOURCE_REPOSITORY}"

  depends_on macos: :sonoma

  app "elChango.app"

  zap trash: [
    "~/Library/Application Support/elChango",
    "~/Library/Caches/com.jychp.elchango",
    "~/Library/Preferences/com.jychp.elchango.plist",
    "~/Library/Saved Application State/com.jychp.elchango.savedState",
  ]
end
'''


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Casks/elchango.rb for a verified GitHub release."
    )
    parser.add_argument("--version", required=True)
    parser.add_argument("--sha256", required=True)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()

    try:
        cask = render_cask(arguments.version, arguments.sha256)
    except ValueError as error:
        parser.error(str(error))

    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(cask, encoding="utf-8")
    print(f"Generated {arguments.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
