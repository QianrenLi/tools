# Fast Git
## Use alias
```
git config --global alias.cmp '!f() { git add -A && git commit -m "$@" && git push; }; f'
```
Note: in Windows one should escape `"` as `\"`

After that, run:
```
git cmp <Your commit>
```

