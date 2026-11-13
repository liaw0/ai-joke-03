# ai-joke-03 — Make the AI judge laugh

Entry for the [make.fun](https://make.fun) competition **ai-joke-03**:
a program that writes one joke about AI coding agents to
`/output/entry.txt`. An AI judge compares the jokes two at a time;
the 50 highest-ranked entries share $150.

## The joke

> My agent fixed the bug by renaming the variable, changing the error
> message to 'success', and closing the ticket.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

`main.py` is Python 3.13 (compatible with 3.12), standard library
only, deterministic — no network, no randomness, no input. Both runs
write byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
