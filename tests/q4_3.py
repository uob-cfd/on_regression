test = {
  'name': 'Question 4_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> contingency_prop.shape
          (5, 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Did you divide each column by the column totals?
          >>> np.isclose(contingency_prop.loc[2, 'married'] * 1484, 373)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
