# tldrgal

> Contribute to [`tldr`](https://github.com/tldr-pages/tldr).

> Inspired by Homebrew's `create`, `edit`, `bump-formula-pr` and `bump-cask-pr`.

> More information: <[INSTALL.md](INSTALL.md)>.

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

- View a page (invokes `tldr {{vim}}`):

`tldrgal view {{vim}}`

- Grep in all files from `tldr`:

`tldrgal grep "{{bad.*user}}"`

- Run `git blame` on a specific page:

`tldrgal blame vim`

- Run a command in the `tldr` repo:

`tldrgal run fd vim`

- Update your fork with upstream changes:

`tldrgal update`
