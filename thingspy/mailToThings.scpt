using terms from application "Mail"
	on perform mail action with messages these_messages for rule this_rule
		tell application "Mail"
			set the message_count to the count of these_messages
			repeat with i from 1 to the message_count
				set this_message to item i of these_messages

				set this_sender to the sender of this_message

				set messageid to message id of this_message
				-- Make URL (must use URL-encoded values for "<" and ">")
				set urlText to "[url=message:%3C" & messageid & "%3E] mail from " & this_sender & " [/url]"

				try
					set this_subject to (subject of this_message) as Unicode text
					if this_subject is "" then error
				on error
					set this_subject to "NO SUBJECT"
				end try

				try
					set this_content to (every character of content of this_message) as Unicode text
					if this_content is in {"", "?"} then error
				on error error_message
					set this_content to "error message:" & error_message
				end try

				set this_content to this_content & "
-------
" & urlText

				tell application "Things3"
					set toDo to make new to do
					set name of toDo to this_subject
					set notes of toDo to this_content
					set tagFromMail to make new tag with properties {name:"From Mail"}
					set tag names of toDo to "From Mail"
				end tell
			end repeat
		end tell
	end perform mail action with messages
end using terms from

