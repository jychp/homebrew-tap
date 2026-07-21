cask "elchango" do
  version "1.1.1"
  sha256 "4c8af31d4d19ddb0cd02a532757ac0faca5c55eae820408a964ade9d95a35d51"

  url "https://github.com/jychp/elchango/releases/download/v#{version}/elChango-#{version}-macos-universal.zip"
  name "elChango"
  desc "Local control deck for native AI coding sessions"
  homepage "https://github.com/jychp/elchango"

  depends_on macos: :sonoma

  app "elChango.app"

  zap trash: [
    "~/Library/Application Support/elChango",
    "~/Library/Caches/com.jychp.elchango",
    "~/Library/Preferences/com.jychp.elchango.plist",
    "~/Library/Saved Application State/com.jychp.elchango.savedState",
  ]
end
