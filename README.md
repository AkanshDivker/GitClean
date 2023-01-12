# GitClean

GitClean is a Python program which goes hand in hand with [GitScrape](https://github.com/AkanshDivker/GitScrape). One of the other common issues when cloning multiple repositories for analysis or research is that you get stuck with a lot of different files that aren't necessary to your purposes. GitClean is a simple script to quickly clean out the files you don't care about, and only keep the files you do care about. 

#### TO-DO:
- Possibly replace log output to file and include progress bar instead
- Use GitClean on the GitClean clean function

## Getting Started

You can get started by cloning the repository on your desktop. The code should be commented enough to follow along and understand. Please install the necessary Python requirements that are located inside of the `requirements.txt` file.

### Prerequisites

This project requires Python 3.7 to be installed. Please ensure the required modules in `requirements.txt` are installed. Should be compatible for all systems that have Python 3.7 properly installed.

### Usage
In order to use the module, cd into the `GitClean` directory and simply start the script by calling `python gitclean.py` in your terminal. A full list of commands and their details can be seen by running `python gitclean.py -h` in your terminal.

An example command to remove all files except Python (.py) files in a directory would be as follows.

```
python gitclean.py -c /home/project -e .py
```

### Final Notes

I created this to help me with collecting repositories for my own research and for optimizing static analysis processing times. I'm always happy to learn, help out, and teach others. If you have any questions or comments, feel free to contact me!

## Authors

* **Akansh Divker** - *Author* - [AkanshDivker](https://github.com/AkanshDivker)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
