package parsinglogfiles

import "regexp"

func IsValidLine(text string) bool {
	re := regexp.MustCompile(`^\[(TRC|DBG|INF|WRN|ERR|FTL)\]`)
	return re.MatchString(text)
}

func SplitLogLine(text string) []string {
	re := regexp.MustCompile(`<[~*=-]*>`)
	return re.Split(text, -1)
}

func CountQuotedPasswords(lines []string) int {
	re := regexp.MustCompile(`(?i)".*password.*`)
	count := 0
	for _, s := range lines {
		if re.MatchString(s) {
			count++
		}
	}
	return count
}

func RemoveEndOfLineText(text string) string {
	re := regexp.MustCompile(`end-of-line\d*`)
	return re.ReplaceAllString(text, "")
}

func TagWithUserName(lines []string) []string {
	re := regexp.MustCompile(`User\s+(\w+)`)

	out := make([]string, len(lines))
	for i, line := range lines {
		m := re.FindStringSubmatch(line)
		if len(m) > 1 {
			// m[1] is the username captured after "User" + spaces
			out[i] = "[USR] " + m[1] + " " + line
		} else {
			out[i] = line
		}
	}
	return out
}
