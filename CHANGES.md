# Changes

## Version 0.1.6:

**date: 2024-09-26**

- missing data interpolation: ensure that u0 is always linearly interpolated
- fix interpolation warning from pandas future deprecation

## Version 0.1.5:

**date: 2024-09-24**

- Add a new interpolation mode for missing values:
  - you can now choose between:
    - "padding" -> propagate last known value in a DataFrame column downward for NaN, only work downward (NaN values at start won't be filled);
    - "linear" -> linearly interpolate missing values based on the last two known, it works both downward and updward.
