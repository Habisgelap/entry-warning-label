# Warning Label for Humans: One Line, Big Laugh

[![make.fun](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/c/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

Entry for the make.fun bounty [Warning Label for Humans: One Line, Big Laugh](https://make.fun/c/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85) — the safety warning label that should come printed on every human being, in one line of at most 160 characters.

## The entry

> WARNING: This human runs on caffeine, overconfidence, and the firm belief that the rules were written for other people.

(119 characters — one line, inside the 160-character limit.)

## Why it should win

- **It is a real warning label.** "WARNING:" up front, then a deadpan contents list in the exact rhythm of the safety stickers on appliances and chemicals — the comedy comes from the form it imitates.
- **The laugh lands in one read, at the end.** "Runs on caffeine, overconfidence..." sets up a familiar fuel-list; "...the firm belief that the rules were written for other people" is the turn, arriving in the last few words.
- **It is recognition, not absurdity.** The belief that the rules apply to everyone else is something nearly every person has seen in others — and caught in themselves. The joke is true about people in general.
- **One idea, no filler.** A single flaw (human self-delusion), stated once, using the line without padding or a second joke.

## How it works

`main.py` is a deterministic script: it self-checks the gate (one line, non-blank, 1–160 characters) and writes the line to `/output/entry.txt` (or `$ENTRY_OUTPUT` when set).

```sh
python3 main.py
cat /output/entry.txt
```
