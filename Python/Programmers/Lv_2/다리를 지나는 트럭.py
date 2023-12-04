from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0

    while bridge:
        total_weight -= bridge.popleft()

        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                truck_weight = truck_weights.pop(0)
                bridge.append(truck_weight)
                total_weight += truck_weight
            else:
                bridge.append(0)

        time += 1

    return time