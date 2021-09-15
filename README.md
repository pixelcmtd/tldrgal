# `tldrgal`

A general Werkzeugkasten to help you contribute to
[`tldr`](https://github.com/tldr-pages/tldr), inspired by Homebrew's
`create`, `edit`, `bump-formula-pr` and `bump-cask-pr`.

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

## Usage

- Now you can create new pages:

`tldrgal add {{obscure_command}}`

- And alias pages:

`tldrgal alias {{python3}}={{python}}`

- Request pages:

```
tldrgal request [command]
tldrgal request llc,lli,llvm-config
```

- Edit pages and other parts of `tldr`:

```
tldrgal edit [command]
tldrgal rawedit [branch-name]
```

- List all commands on your system that don't have a `tldr` page yet:

`tldrgal missing`

- Find all files in `tldr` that match a regex (useful for example for finding all
languages that a page has been translated to):

```
tldrgal find 'llvm-.*'
tldrgal find vim
```

- View a page (currently uses `view`, which is installed by `vim`):

`tldrgal view vim`

- Remove branches:

`tldrgal rm {{clangxx}}`

- Update your fork with upstream changes:

`tldrgal update`
