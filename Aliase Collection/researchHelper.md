# ResearchHelper
## pdf2emf
There are times when picture in pdf format is not accepted and only emf is required. Here are the alias that processing the pdf to emf.
```bash
alias pdf2emf='function convert_pdf_to_emf_fn() { for file in "$@"; do pdf2svg "$file" temp.svg && inkscape temp.svg -M "${file%.pdf}.emf"; done; rm temp.svg; }; convert_pdf_to_emf_fn'
``` 
