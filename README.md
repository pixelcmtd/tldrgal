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

- Find all pages that start with "llvm-":

`tldrgal find {{llvm-}}`

- Find all translations of the `vim` page:

`tldrgal find '^{{vim}}.md$'`

- View a page (currently uses `view`, which is installed by `vim`):

`tldrgal view {{vim}}`

- Remove a branch:

`tldrgal rm {{clangxx}}`

- Grep in all files from `tldr`:

`tldrgal grep "{{bad.*user}}"`

- Check out a specific branch without doing anything else:

`tldrgal checkout {{my-branch}}`

- Update your fork with upstream changes:

`tldrgal update`
