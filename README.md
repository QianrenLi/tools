# tools

## Global listener in pix2tex

The pix2tex works great in latex ocr, the problem is the hotkey applied only valid when the gui is focused.
This tool mainly modify the [gui.py](https://github.com/QianrenLi/tools/blob/master/gui_latexocr/gui.py) to result better experience.

### Requirement

1. package keyboard: 

```matlab
pip install keyboard
```

1. latexocr

[https://github.com/lukas-blecher/LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR)

### Procedure

1. Identify the location of pix2tex

![image](https://user-images.githubusercontent.com/51881852/198520201-051e1b8e-2797-45e7-937a-4c91e126cb62.png)


2. Replace [gui.py](https://github.com/QianrenLi/tools/blob/master/gui_latexocr/gui.py) with given file
3. Run the result with cmd: 
```
python -m pix2tex.__main__ --gui
```
or modifying the .bat file to match your environemnt
