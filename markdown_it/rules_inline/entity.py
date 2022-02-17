# Process html entity - &#123;, &#xAF;, &quot;, ...
import re

from ..common.entities import entities
from ..common.utils import has, isValidEntityCode, fromCodePoint
from .state_inline import StateInline

DIGITAL_RE = re.compile(r"^&#((?:x[a-f0-9]{1,6}|[0-9]{1,7}));", re.IGNORECASE)
NAMED_RE = re.compile(r"^&([a-z][a-z0-9]{1,31});", re.IGNORECASE)


def entity(state: StateInline, silent: bool):

    pos = state.pos
    maximum = state.posMax

    if state.srcCharCode[pos] != 0x26:  # /* & */
        return False

    if (pos + 1) < maximum:
        ch = state.srcCharCode[pos + 1]

        if ch == 0x23:  # /* # */
            if match := DIGITAL_RE.search(state.src[pos:]):
                if not silent:
                    match1 = match.group(1)
                    code = (
                        int(match1[1:], 16)
                        if match1[0].lower() == "x"
                        else int(match1, 10)
                    )
                    state.pending += (
                        fromCodePoint(code)
                        if isValidEntityCode(code)
                        else fromCodePoint(0xFFFD)
                    )

                state.pos += len(match.group(0))
                return True

        elif match := NAMED_RE.search(state.src[pos:]):
            if has(entities, match.group(1)):
                if not silent:
                    state.pending += entities[match.group(1)]
                state.pos += len(match.group(0))
                return True

    if not silent:
        state.pending += "&"
    state.pos += 1
    return True
