# Animpy v2.5.0

Release: 2026-05-23

Highlights
- Bumped package version to `2.5.0`.
- Added small utility helpers across core classes:
  - `Coords.distance_to`, `Coords.offset`
  - `Keyframe.set_pos`, `Keyframe.distance_to`, `KeyChains.append/clear/reverse_path/is_complete`
  - `Audio.pause/resume/fade_in/fade_out`
  - `Group.clear/contains/find_by_color`
  - `Particle.set_velocity/apply_force/set_color/reset/is_alive`
  - `Scene.clear_items/count_items/find_items_at`, physics/wind helpers
  - `Shapes.square` and `Shapes.donut` and fixed newline handling
  - `Text` convenience setters and `type_out`, `fall`
  - `EffectText` velocity helpers and `fade_in_text`

Testing
- All unit tests pass locally: `36 passed`.

Docs
- Updated `README.md` and `animpy-docs` with v2.5.0 notes and API changes.
- Built the MkDocs site locally (output in `animpy/animpy-docs/site`).

Publishing suggestions
- To commit & tag locally:

```
git add .
git commit -m "chore(release): v2.5.0 — helpers and docs"
git tag -a v2.5.0 -m "v2.5.0"
git push && git push --tags
```

- To build and upload to PyPI (optional):

```
python -m build
python -m twine upload dist/*
```

- To deploy docs with MkDocs (Material) to GitHub Pages:

```
mkdocs gh-deploy -f animpy/animpy-docs/mkdocs.yml
```
