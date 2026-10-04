# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pyweblight/main.py:12-23` - the `start` and `stop` endpoints are bare `pass`, so the installed `pyweblight` command does nothing; the real server lives in `webserver_start.py`/`webserver_stop.py` and is only reachable via `python -m`. Wire `start` to `webserver_start.main()` (inside the `daemon.DaemonContext()` now at `webserver_start.py:195`) and `stop` to `webserver_stop.main()`.
- `src/pyweblight/webserver_start.py:41` - `do_QUIT` calls `self.server.set_stop()`, but `StoppableHttpServer` (`webserver_start.py:165-176`) defines no such method, only a `stop` attribute; every QUIT request raises `AttributeError`, so `webserver_stop` can never stop the server. Add `def set_stop(self): self.stop = True` to `StoppableHttpServer` (or set `self.server.stop = True` directly), and add a test for it.

## Medium

- `src/pyweblight/webserver_start.py:103-122` - `get()` resolves the path through `search_path` but then calls `handle_dir(real_path)` with the unresolved path, so a directory found under `/usr/share/javascript` makes `os.listdir` fail and the request returns 500. Pass `resolved`.
- `src/pyweblight/webserver_start.py:83-90` - `to_path()` uses `self.path[1:]` raw: query strings are not stripped (`/a.html?x=1` gives 404) and `..` segments are not rejected, so `/../../etc/passwd` is served (the comment at lines 52-54 admits this). Parse with `urllib.parse.urlsplit`, `unquote`, normalize, and reject paths that escape the search folders.
- `src/pyweblight/webserver_start.py:79-81` - the `.esp` page prints `str(time)` (the module repr) as "time", and the two labels are swapped: `localtime()[7]` is the day of the year and `localtime()[0]` is the year. Use `time.ctime()` and fix the labels.
- `src/pyweblight/webserver_start.py:147` - a successful POST answers `301` with no `Location` header; it should be `200`.
- `src/pyweblight/webserver_start.py:27-30` and `pyproject.toml:107` - the `except ImportError` fallback imports `multipart.parse_form`, which does not exist in the declared `multipart` package, and is the signature-incompatible `python-multipart` API when that package wins. `python-multipart` (dev group) is used by no code or test, yet installs its own `multipart/` package over the same import name as the runtime `multipart` dependency. Drop `python-multipart` from the dev group and delete the fallback import.

## Low

- `src/pyweblight/configs.py:9` - `ConfigForce` is never imported or used anywhere; delete the module (and its entry in `sphinx/pyweblight.rst`) or use it.
- `src/pyweblight/webserver_start.py:97-100` - directory listing writes file names into HTML unescaped and hardcodes `http://localhost:8001` (a no-op anyway because `self.path` is absolute). Use `html.escape` and `urllib.parse.quote`, and relative links.
- `src/pyweblight/webserver_start.py:151` - uploaded content is echoed into HTML unescaped; wrap it in `html.escape`.
- `src/pyweblight/webserver_start.py:63` - `f.close()` inside the `with` block is redundant; remove it.
- `src/pyweblight/webserver_start.py:158-162` - `log_message` swallows all request logs (the module TODO at line 10 wants them in a log file); log through `logging.getLogger(LOGGER_NAME)`.
- `src/pyweblight/webserver_start.py:8-20` - the module docstring carries a stale TODO list (rename to "dws", favicon 500, strip params) that duplicates the real bugs above; move what is still valid to `doc/TODO.txt` (currently empty) and delete the rest.
- `pyproject.toml:84` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/` directories that do not exist; use `"src"`.
