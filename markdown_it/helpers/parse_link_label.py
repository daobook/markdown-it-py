"""
Parse link label

this function assumes that first character ("[") already matches
returns the end of the label

"""
from markdown_it.rules_inline import StateInline


def parseLinkLabel(state: StateInline, start: int, disableNested: bool = False) -> int:

    oldPos = state.pos
    found = False

    state.pos = start + 1
    level = 1

    while state.pos < state.posMax:
        marker = state.srcCharCode[state.pos]
        if marker == 0x5D:  # /* ] */)
            level -= 1
            if level == 0:
                found = True
                break

        prevPos = state.pos
        state.md.inline.skipToken(state)
        if prevPos == state.pos - 1:
            if marker == 0x5B:
                # increase level if we find text `[`,
                # which is not a part of any token
                level += 1
        elif disableNested:
            if marker == 0x5B:
                state.pos = oldPos
                return -1
    labelEnd = state.pos if found else -1
    # restore old state
    state.pos = oldPos

    return labelEnd
