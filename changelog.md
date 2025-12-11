# Changelog

## [0.3] - 2025-12-11

- `DocContext` was renamed to `Context`
- Custom fields support in path templates was removed
- Instead of `{{ document.title }}` now is `{{ title }}`
- Implicit home folder of the owner is assumed i.e. no need to type `/home/...`

## [0.2.1] - 2025-08-04

### Changes

- updated external libraries

## [0.2] - 2024-11-24

### Changes

- `get_evaluated_path` returns just a string (instead of PurePath instance)
