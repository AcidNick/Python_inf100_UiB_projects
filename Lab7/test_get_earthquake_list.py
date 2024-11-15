from earthquakes import get_earthquake_list

def test_get_earthquake_list():
    print('Testing get_earthquake_list...', end=' ')
    s = '''\
time,latitude,longitude,depth,mag,magType,nst,gap,dmin,rms,net,id,updated,place,type,horizontalError,depthError,magError,magNst,status,locationSource,magSource
2024-03-13T15:13:23.771Z,-5.8705,150.6344,50.416,6,mww,112,33,9.887,0.95,us,us6000milg,2024-03-14T15:22:18.952Z,"65 km ESE of Kimbe, Papua New Guinea",earthquake,8.18,4.68,0.044,49,reviewed,us,us
2024-03-14T21:10:24.838Z,29.8022,-42.6586,10,6,mww,179,57,16.293,0.61,us,us6000miy6,2024-03-18T01:11:06.363Z,"northern Mid-Atlantic Ridge",earthquake,9.76,1.795,0.039,62,reviewed,us,us
2024-03-16T00:14:52.156Z,-58.9182,158.3605,10,5.9,mww,58,55,4.443,0.51,us,us6000mj77,2024-03-17T19:46:20.040Z,"Macquarie Island region",earthquake,10.98,1.829,0.071,19,reviewed,us,us
2024-03-13T18:56:13.292Z,-0.1127,125.2136,26.46,5.8,mww,89,67,2.325,1.16,us,us6000minw,2024-03-14T19:00:56.901Z,"106 km SE of Modisi, Indonesia",earthquake,7.48,4.881,0.068,21,reviewed,us,us
'''
    expected = [
        (150.6344, -5.8705, 6),
        (-42.6586, 29.8022, 6),
        (158.3605, -58.9182, 5.9),
        (125.2136, -0.1127, 5.8),
    ]
    actual = get_earthquake_list(s)
    assert actual == expected, f'Expected {expected}, but got {actual}'
    print('OK')

if __name__ == '__main__':
    test_get_earthquake_list()
