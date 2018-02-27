def are_ordered_units(x, y):
  """Return true if x < y and both are in [0, 1]"""
  return 0 <= x < y <= 1
