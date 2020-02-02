# EPstripper

This is a short script that can be used to strip/redact entrypoints from malware samples in order to defang them.

## Why?

While going through [Malware Data Science](https://www.malwaredatascience.com/), I noticed that the malware samples included in the book's 'code and data' download had their entry points redacted.

![book_code_download](/media/book_code_download.png)
![show_ep_value](/media/show_ep_value.png)

I'm assuming this was done so that live samples wouldn't be hosted directly from the site, or so that people working through the book would be unable to accidently infect themselves.

I thought it would be a nice exercise to create a tool to do this for a given directory of samples.

## Example

![example_before](/media/example_before.png)
![example_command](/media/example_command.png)
![example_after](/media/example_after.png)


## Installation

EPstripper uses Python 3

```
git clone https://github.com/patrickarmengol/EPstripper.git
cd EPstripper
pip install pefile
```

- [pefile](https://github.com/erocarrera/pefile)


## Usage

> please note this does not overwrite the original files, it creates copies

> if you pass it a directory, it will walk through all subdirectories

> the script ignores non PE files

```
usage: epstripper.py [-h] [-r EP_VAL] input

a script to replace the entrypoint of a PE file

positional arguments:
  input       input file or directory

optional arguments:
  -h, --help  show this help message and exit
  -r EP_VAL   specify replacement value - else will use default 0xcc00ffee
```

## Todo

- add a way to dump to a file a dictionary of original entry points so that they may be reconstructed

- add an output directory to collect all the stripped files (maybe keep subdirectory structure??)
