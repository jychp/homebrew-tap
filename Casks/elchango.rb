cask "elchango" do
  version "1.1.0"
  sha256 "99678b964ad16b1e47b5a808ce239c6c41e45db7ed211a800bf291752b57ddec"

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
