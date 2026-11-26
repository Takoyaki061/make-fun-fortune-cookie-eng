# Fortune Cookie Funnies for Engineers

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/Takoyaki061/make-fun-fortune-cookie-eng/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/Takoyaki061/make-fun-fortune-cookie-eng/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)

An entry for the [Fortune Cookie Funnies for Engineers](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a) bounty on make.fun: one funny fortune cookie message for a software engineer, at most 120 characters, judged head-to-head against other fortunes.

## The fortune

`main.py` writes this to `/output/entry.txt`:

> Your rubber duck has known the answer for twenty minutes and is waiting for you to finish.

Rubber-duck debugging is the one ritual every engineer actually does: you explain the bug out loud to a duck on your desk and the answer arrives mid-sentence. The fortune turns the duck from a prop into a person — it knew the answer twenty minutes ago and has been politely waiting for you to catch up. The reader is the butt of the joke (slow, not the duck), which is why it lands warm instead of mean, and the punchline is the last word: "finish".

## How it works

`main.py` (stdlib only, deterministic) holds the fortune as a constant, checks it against the kit's gate — 1 to 120 characters, a single line, not only whitespace — and only then writes it to `/output/entry.txt`. A fortune that would fail the sealed scorer fails loudly here instead.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
