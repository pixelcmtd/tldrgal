# Installing `tldrgal`

## Dependencies

- Python 3 (just use the newest one)
- `fd`
- `$SHELL` or `bash`
- `$EDITOR` or `vi`
- `view`
- `xdg-open` on Linux, `open` otherwise
- `git`
- `npm`

## Setup

Create a file in your home under `.config/tldrgal/username` with your GitHub
username, like this:

```sh
mkdir -p ~/.config/tldrgal
echo random_developer > ~/.config/tldrgal/username
```

Replace `random_developer` with the user or organisation, to which you have
forked the `tldr` repository.

Since we aren't on PyPI right now, installing `tldrgal` itself is a bit manual:
Either clone this repo and add it to your `PATH` (recommended) or just drop the
`tldrgal` script into some directory from your `PATH`.
