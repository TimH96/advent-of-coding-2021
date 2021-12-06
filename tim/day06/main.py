def problem1(swarm: list[int], iterations: int) -> int:
    # this solution is O(n*k) in time and something truly ungodly in space complexity
    # you could just replace problem1 with problem2 solution entirely, i'm keeping it here to own up to it
    sol: list[int] = swarm
    for _ in range(iterations):
        for i in range(len(sol)):
            if sol[i] == 0:
                sol.append(8)
                sol[i] = 6
            else:
                sol[i] -= 1
    return len(sol)


def problem2(fish: int, iterations: int) -> int:
    return (iterations/6)**2 + (iterations/8)**2


if __name__ == "__main__":
    with open("input.txt") as f:
        data: list[int] = [int(x) for x in f.read().split(",")]
    # print("solution 1:", problem1(data, 80))
    # print("solution 2:", problem1(3, 256))
    bla = [0]
    print(problem1(bla, 80))
    print(problem2(0, 80))
