# docsbuilder venv

Detailes steps on how to setup docsbuilder virtual envoronment. Why we need it, because of this error that Poetry gives on dependency resoultion:

Resolving dependencies...

  SolverProblemError

  Because no versions of mkdocs match >1.3.0,<2.0.0
   and mkdocs (1.3.0) depends on importlib-metadata (>=4.3), mkdocs (>=1.3.0,<2.0.0) requires importlib-metadata (>=4.3).
  And because flake8 (4.0.1) depends on importlib-metadata (<4.3)
   and no versions of flake8 match >4.0.1,<5.0.0, mkdocs (>=1.3.0,<2.0.0) is incompatible with flake8 (>=4.0.1,<5.0.0).
  So, because fakenos depends on both flake8 (^4.0.1) and mkdocs (^1.3.0), version solving failed.

  at ~\AppData\Roaming\pypoetry\venv\lib\site-packages\poetry\puzzle\solver.py:241 in _solve
      237│             packages = result.packages
      238│         except OverrideNeeded as e:
      239│             return self.solve_in_compatibility_mode(e.overrides, use_latest=use_latest)
      240│         except SolveFailure as e:
    → 241│             raise SolverProblemError(e)
      242│
      243│         results = dict(
      244│             depth_first_search(
      245│                 PackageNode(self._package, packages), aggregate_package_nodes
	  
In other owrjds - mkdocs (>=1.3.0,<2.0.0) is incompatible with flake8 (>=4.0.1,<5.0.0), where flake8 is part of dev dependencies,
was not able to resolve it using poetry extras or using optional keyword in dependency specifications, even if specify optional
for noth flake8 and mkdocs - poetry still tries to resolve them both. Tried moving all to extras under main dependencies - still the same error.

## Create docsbuilder environment
python3 -m venv docsbuilder

## Activate docsbuilder environment
cd docsbuilder
cd Scripts
activate

## Update pip installation
python3 -m pip install pip --upgrade

## Install fakenos without dev dependencies
cd ../../
poetry install --no-dev

## Install mkdoc requirements 
python3 -m pip install mkdocs==1.3.0 mkdocstrings==0.18.1 mkdocs-material mkdocstrings[python]>=0.18

## Useful resources

https://squidfunk.github.io/mkdocs-material/creating-your-site/#minimal-configuration
https://www.mkdocs.org/getting-started/ 
https://mkdocstrings.github.io/ - main mkdocstring website
https://mkdocstrings.github.io/python/usage/#handler-options - mkdocstring python handler usage