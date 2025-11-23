To reproduce the SQLAlchemy error, run `pants test ::` or `pants run main.py`

Also reproduces with `uv run main.py`.

However, doesn't reproduce with vanilla venv:
```bash
> python -m venv .venv
> source .venv/bin/activate
> pip install -r requirements.txt
> python main.py
> pytest test_bq.py
```
