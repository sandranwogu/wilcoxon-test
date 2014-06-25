def get_table(n):
  if n == 0:
    return [[1.0]]
  elif n == 1:
    return [
            [1.0, 0.0],
            [0.5, 0.5]
           ]
  elif n == 2:
    return [
            [1.0, 0.0, 0.0, 0.0],
            [0.5, 0.5, 0.0, 0.0],
            [0.5, 0.5, 0.25, 0.25]
           ]
  elif n == 5:
    return [
            [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.5, 0.5, 0.25, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.625, 0.375, 0.375, 0.25, 0.25, 0.125, 0.125, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.5625, 0.4375, 0.4375, 0.3125, 0.3125, 0.1875, 0.1875, 0.125, 0.125, 0.0625, 0.0625, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.5, 0.5, 0.40625, 0.40625, 0.3125, 0.3125, 0.21875, 0.21875, 0.15625, 0.15625, 0.09375, 0.09375, 0.0625, 0.0625, 0.03125, 0.03125]
           ]
  else:
    raise Exception("Invalid n")
