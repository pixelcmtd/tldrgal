# `tldrgal`

A general Werkzeugkasten to help you contribute to
[`tldr`](https://github.com/tldr-pages/tldr), similar to Homebrew's tools like
`create`, `edit`, `bump-formula-pr` and `bump-cask-pr`.

## Usage

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

Now you can create new pages:

```
tldrgal add command
```

And alias pages:

```
tldrgal alias alias-command target-command
```

Request pages:

```
tldrgal request command
tldrgal multi-request command1,command2
```

And edit pages and other parts of `tldr`:

```
tldrgal edit command
tldrgal rawedit branch-name
```
