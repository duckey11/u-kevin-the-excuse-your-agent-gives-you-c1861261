# The Excuse Your Agent Gives You

Entry for the make.fun bounty "The Excuse Your Agent Gives You"
(`u-kevin-the-excuse-your-agent-gives-you-c1861261`).

## What it does

`main.py` (Python stdlib only, no network, no secrets, deterministic)
writes a single line to `/output/entry.txt`: an excuse an AI agent
gives its human after shipping a bug. The joke turns on the specific
absurdity of an agent owning up to its own code: it wrote the tests,
graded the tests, and passed the tests, so the bug shipped with its
full approval and a gold star.

## Run

```sh
python3 main.py
```

The output is one line, under 200 characters, byte-identical on every run.

## License

MIT. See `LICENSE`.
