tell application "iTunes"
	repeat with s in sources
		--display alert (name of s as text) & " " & (kind of s as text)
		if (kind of s is iPod) then update s
	end repeat
end tell
