# Release Notes

## v2.5.0 — 2026-05-23

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

- README and API docs updated to reflect the new helpers and examples.

See the full `RELEASE_NOTES.md` at the project root for more details.
