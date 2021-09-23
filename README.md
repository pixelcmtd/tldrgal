# `tldrgal`

A general Werkzeugkasten to help you contribute to
[`tldr`](https://github.com/tldr-pages/tldr), inspired by Homebrew's
`create`, `edit`, `bump-formula-pr` and `bump-cask-pr`.

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

## Usage

- Create a new page:

`tldrgal add {{obscure_command}}`

- Create an alias page:

`tldrgal alias {{python3}}={{python}}`

- Request pages:

`tldrgal request {{llc,lli,llvm-config}}`

- Edit a page:

`tldrgal edit {{command}}`

- Make an edit that isn't contrained to a single page:

`tldrgal rawedit {{blow-everything-up}}`

- List all commands on your system that don't have a `tldr` page yet:

`tldrgal missing`

- Find all files in `tldr` that match a regex (useful for example for finding all
languages that a page has been translated to):

- Find all pages that start with "llvm-":

`tldrgal find llvm-`

- Find all translations of the `vim` page:

`tldrgal find '^vim.md$'`

- View a page (currently uses `view`, which is installed by `vim`):

`tldrgal view vim`

- Remove a branch:

`tldrgal rm {{clangxx}}`

- Grep in all files from `tldr`:

`tldrgal grep "{{bad.*user}}"`

- Check out a specific branch without doing anything else:

`tldrgal checkout {{my-branch}}`

- Update your fork with upstream changes:

`tldrgal update`
