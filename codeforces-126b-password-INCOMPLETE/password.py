import fileinput

def main():
    s = fileinput.input()[0].strip()

    valid_fixes = []
    start       = 0
    end         = len(s) - 1
    prefix_end  = 0

    print("word is: {} of length: {}".format(s, len(s)))
    while start < len(s):
        if s[start] == s[end]:
            # validate prefix matches suffix
            match = True
            i     = start - 1
#             end  -= 1

            while match and i >= prefix_end:
                print("validating; start = {}, i = {}, end = {}, prefix_end = {}".format(start, i, end, prefix_end))
                # check from right to left on the prefix
                # and the suffix
                if s[i] == s[end - 1]:
                    i   -= 1
                    end -= 1
                else:
                    print("prefix '{}' does not match suffix '{}'".format(s[:start + 1], s[end:]))
                    match = False
            if not match:
                # no more prefixes & suffixes can possibly match
                break
            else:
                print("Validated prefix '{}' to suffix '{}'".format(s[:start + 1], s[end:]))
                valid_fixes.append(s[:start + 1])
                prefix_end = start + 1

        # continue hunting for a prefix that ends with suffix
        start += 1

    printed = False
    print("Checking the following valid_fixes: {}".format(valid_fixes))
    while valid_fixes and not printed:
        fix = valid_fixes.pop()
        if fix in s[1:len(s) - 1]:
            print(fix)
            printed = True

    if not printed:  # never found a valid prefix, suffix, and interior match
        print("Just a legend")

main()
