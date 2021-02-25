test = {
  'name': 'Question 3_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You should return two parameters from your function.
          >>> out = regression_parameters(jumps)
          >>> # You should return two parameters from your function.
          >>> len(out)
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You should have two parameters.
          >>> len(parameters)
          2
          >>> # The intercept doesn't look quite right.
          >>> np.isclose(parameters[0], -1.566513)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # This is a copy of the data frame, with the columns renamed.
          >>> jumps_renamed = jumps.copy()
          >>> jumps_renamed.columns = ['a', 'b']
          >>> # Your function should get the *first* and *second* columns,
          >>> # and not rely on particular column names.  Check the Pandas
          >>> # pages on getting columns by column position.
          >>> out = regression_parameters(jumps_renamed)
          >>> np.isclose(out[0], -1.566513)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
