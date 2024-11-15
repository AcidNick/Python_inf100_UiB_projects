from pathlib import Path
from earthquakes import load_coastlines

def test_load_coastline():
    path = Path('ne_110m_coastline.json')
    org_data = None
    if path.is_file():
        org_data = path.read_bytes()
    try:
        do_test_load_coastline(path)
    finally:
        path.unlink(missing_ok=True)
        if org_data is not None:
            path.write_bytes(org_data)

def do_test_load_coastline(path: Path):
    print('Testing load_coastline...', end='')
    arg = '''\
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "scalerank": 1,
        "featurecla": "Coastline",
        "min_zooom": 1.0
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [ -163.71289567772871, -78.595667413241543 ],
          [ -159.482404548154477, -79.046337579258974 ],
          [ -163.027407803377002, -78.928773695794959 ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "scalerank": 0,
        "featurecla": "Coastline",
        "min_zooom": 0.0
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [ -6.197884894220991, 53.867565009163364 ],
          [ -9.977085740590269, 51.820454820353078 ],
          [ -7.572167934591064, 55.131622219454869 ]
        ]
      }
    }
  ]
}
'''
    path.write_text(arg)
    expected = [ 
        [ # Første øy
            [ -163.71289567772871, -78.595667413241543 ],
            [ -159.482404548154477, -79.046337579258974 ],
            [ -163.027407803377002, -78.928773695794959 ]
        ],
        [ # Andre øy
            [ -6.197884894220991, 53.867565009163364 ],
            [ -9.977085740590269, 51.820454820353078 ],
            [ -7.572167934591064, 55.131622219454869 ]
        ]
    ]
    actual = load_coastlines()
    assert expected == actual, f'Expected {expected}, but got {actual}'
    print('OK')

if __name__ == '__main__':
    test_load_coastline()
