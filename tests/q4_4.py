test = {
  'name': 'Question 4_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # tvd_marriages should be a single number.
          >>> np.array(tvd_marriages).size
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(tvd_marriages, 2)
          0.19
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
