# Alias collection
## Fast Git
```bash
git config --global alias.cmp '!f() { git add -A && git commit -m "$@" && git push; }; f'
```
Note: in Windows one should escape `"` as `\"`

After that, run:
```bash
git cmp <Your commit>
```

## Clean and clone
Sometimes clean repo and reclone it is necessary, i mean especially when you deal with remote server under unprotect system, that is, sharing the data with others.

Although a full virtualization might be a better solution, here a simple alias designed to remove git repo and fast clone is introduced.

``` bash
git ls-files -z --ignored --exclude-standard | xargs -0 git rm -r --cached .; git clean -f;rm -rf .git

x(){ var="$1"; git clone git@github.com:QianrenLi/${var::-1}.git temp ; mv temp/.git "$1".git; rm -rf temp; cd "$1"; git reset --hard; }; x
```
- The first one `gitclean` (for example) is mainly used to clear all the code and git repo while keeping untracked file.

- The Second one `gitclone` is used to clone the repo to an exsiting folder.

Worth noticing that, when useing ssh remote server with multi-user, you might want to combine the ssh-agent by adding fastforward keyword and git local by simple alias:
``` bash
git config --local user.email \"Your email\";git config --local user.name \"Your Name\"
```