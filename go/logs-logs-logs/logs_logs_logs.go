package logs

import (
	"unicode/utf8"
)

var appByRune = map[rune]string{
	'❗': "recommendation",
	'🔍': "search",
	'☀': "weather",
}
var defaultApp = "default"

// Application identifies the application emitting the given log.
func Application(log string) string {
	for _, r := range log {
		if app, exists := appByRune[r]; exists {
			return app
		}
	}
	return defaultApp
}

// Replace replaces all occurrences of old with new, returning the modified log
// to the caller.
func Replace(log string, oldRune, newRune rune) string {
	if oldRune == newRune {
		return log
	}
	runes := []rune(log)
	for i, r := range runes {
		if r == oldRune {
			runes[i] = newRune
		}
	}
	return string(runes)
}

// WithinLimit determines whether or not the number of characters in log is
// within the limit.
func WithinLimit(log string, limit int) bool {
	return utf8.RuneCountInString(log) <= limit
}
