# Uses python3
import sys
from collections import namedtuple
import pdb


Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []

    while(len(segments) > 0):
        remove_list = []
        min_right = choose_min_right_segment(segments)
        points.append(min_right)
        for s in segments:
            # print("s = ",s.start,s.end,"with min_right",min_right)
            # pdb.set_trace()
            if include_point(s, min_right):
                remove_list.append(s)
        for r in remove_list:
            segments.remove(r)

    return points

def include_point(segment, point):
    # print("start",segment.start,"end",segment.end)
    if segment.start <= point <= segment.end:
        # print('here')
        return True
    else:
        # print("never here")
        return False

def choose_min_right_segment(segments):
    segments = sorted(segments, key=lambda x: x.end)
    return segments[0].end

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
