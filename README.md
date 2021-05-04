# leetcode_problem_setup

Setting up local python environment, making sure to use `python3`
to create the virtualenv. After activating, future `python` commands
should use that version of Python by default.

```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

For Windows:

```
py -m venv .venv
source .venv/Scripts/activate
py -m pip install -r requirements.txt
py main.py
```
