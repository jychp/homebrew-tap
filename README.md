# Jychp Tap

## Install elChango

elChango is distributed as a signed and notarized Universal 2 macOS
application:

```bash
brew install --cask jychp/tap/elchango
```

To upgrade after a new release:

```bash
brew update
brew upgrade --cask elchango
```

The Cask requires macOS 14 or newer. It installs `elChango.app` in
`/Applications`. Uninstalling preserves user preferences; use
`brew uninstall --zap elchango` to remove elChango preferences, caches, and
application support data as well.

Each elChango GitHub release dispatches an update to this tap. Automation
downloads the public release and checksum, opens a pull request, and requests
auto-merge. Intel and Apple Silicon checks audit the Cask, install the app, and
verify its Developer ID signature, stapled notarization ticket, and Gatekeeper
acceptance before GitHub can merge the update.

If an update pull request fails, the existing Cask remains unchanged. Fix the
release or automation issue, then redispatch the same version; generation is
idempotent.

## Other formulae

Install another formula with `brew install jychp/tap/<formula>`, or run
`brew tap jychp/tap` first and use its short name.
