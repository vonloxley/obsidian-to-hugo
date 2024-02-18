"""
Utilities to extract markdown bBllockquotes from text and fix them for obsidian
by adding two spaces at the end of each line.
"""

from typing import TypedDict, List
import re

BlockQuoteLine = TypedDict("BlockQuoteLines", {"bcl": str})

def get_md_bql(text: str) -> List[BlockQuoteLine]:
    bcls = []
    bcl_regex = r"(?m)^> .*$"
    for match in re.finditer(bcl_regex, text):
        out = {
            "bcl": match.group(),
        }
        bcls.append(out)
    return bcls


def md_bcls_to_html_bcls(bcl: BlockQuoteLine) -> str:
    html_bcl = f'{bcl["bcl"]}  '
    return html_bcl


def replace_md_blockquotes(text: str) -> str:
    marks = get_md_bql(text)
    for mark in marks:
        html_mark = md_bcls_to_html_bcls(mark)
        text = text.replace(mark["bcl"], html_mark)
    
    return text
