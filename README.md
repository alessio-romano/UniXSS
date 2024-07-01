<h1 align="center"> UniXSS.py <br> </h1>

<h4 align="center">Leverage Unicode Normalization to gain XSS</h4>

<p align="center">
  <a href="#install-">Install</a> •
  <a href="#get-started-">Get Started</a> •
  <a href="#examples-">Examples</a>
</p>

----------
  
Install 💻
----------

Use the `requirements.txt` file:

```console
pip3 install -r requirements.txt
```


Get Started 📚
----------

```
Usage: python3 UniXSS.py [input_payload] [optional_arguments]

positional arguments:
  input_text      The text to be transformed

optional arguments:
  -h, --help      show this help message and exit
  --table         Print the character mapping table
  --only-special  Only process special characters
```


Examples 🔎
----------

Perform UniCode Normalization

```bash
python3 UniXSS.py "<script>alert(1)</script>"
```

Perform UniCode Normalization and print the character mapping table

```bash
python3 UniXSS.py "<script>alert(1)</script>" --table
```

Perform UniCode Normalization, only applied to the payload's special characters

```bash
python3 UniXSS.py "<script>alert(1)</script>" --only-special
```

Perform UniCode Normalization and print the character mapping table, only on special characters

```bash
python3 UniXSS.py "<script>alert(1)</script>" --only-special --table
```

---------





