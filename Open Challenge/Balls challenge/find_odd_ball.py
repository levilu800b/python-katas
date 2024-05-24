import matplotlib.pyplot as plt
import numpy as np


def weigh(group1, group2):
    weight1 = sum(group1)
    weight2 = sum(group2)
    if weight1 == weight2:
        return 0
    return 1 if weight1 > weight2 else -1


def findOddBall(balls):
    steps = []

    def record_step(groupA, groupB, groupC, result, step_desc):
        steps.append({
            "groupA": groupA,
            "groupB": groupB,
            "groupC": groupC,
            "result": result,
            "desc": step_desc
        })

    groupA = balls[:4]
    groupB = balls[4:8]
    groupC = balls[8:]

    result1 = weigh(groupA, groupB)
    record_step(groupA, groupB, groupC, result1, "Weigh group A vs group B")

    if result1 == 0:
        result2 = weigh([groupC[0]], [groupC[1]])
        record_step([groupC[0]], [groupC[1]], groupC[2:], result2, "Weigh ball 9 vs ball 10")

        if result2 == 0:
            result3 = weigh([groupC[2]], [groupA[0]])
            record_step([groupC[2]], [groupA[0]], [groupC[3]], result3, "Weigh ball 11 vs ball 1")

            if result3 == 0:
                odd_ball = 12
                odd_weight = "heavier" if balls[11] > 1 else "lighter"
            else:
                odd_ball = 11 if result3 == 1 else 12
                odd_weight = "heavier" if result3 == 1 else "lighter"
        else:
            result3 = weigh([groupC[0]], [groupA[0]])
            record_step([groupC[0]], [groupA[0]], [groupC[1]], result3, "Weigh ball 9 vs ball 1")

            if result3 == 0:
                odd_ball = 10
                odd_weight = "heavier" if result2 == 1 else "lighter"
            else:
                odd_ball = 9 if result2 == result3 else 10
                odd_weight = "heavier" if result2 == result3 else "lighter"
    else:
        suspectGroup = groupA if result1 == 1 else groupB
        otherGroup = groupB if result1 == 1 else groupA

        result2 = weigh(suspectGroup[:3], otherGroup[:3])
        record_step(suspectGroup[:3], otherGroup[:3], suspectGroup[3:], result2, "Weigh suspected group vs other group")

        if result2 == 0:
            odd_ball = 4 if result1 == 1 else 8
            odd_weight = "heavier" if result1 == 1 else "lighter"
        else:
            subGroup1 = suspectGroup[:2]
            subGroup2 = otherGroup[:2]

            result3 = weigh(subGroup1, subGroup2)
            record_step(subGroup1, subGroup2, suspectGroup[2:], result3, "Weigh subgroups")

            if result3 == 0:
                odd_ball = suspectGroup[2]
                odd_weight = "heavier" if result1 == 1 else "lighter"
            else:
                if result3 == result1:
                    odd_ball = suspectGroup[0]
                    odd_weight = "heavier" if result1 == 1 else "lighter"
                else:
                    odd_ball = suspectGroup[1]
                    odd_weight = "heavier" if result1 == 1 else "lighter"

    return odd_ball, odd_weight, steps


def visualize(steps):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i, step in enumerate(steps):
        ax.clear()
        ax.set_title(f"Step {i + 1}: {step['desc']}")

        for j, (group, color) in enumerate(zip([step['groupA'], step['groupB'], step['groupC']], ['r', 'g', 'b'])):
            xs = np.full(len(group), j)
            ys = np.arange(len(group))
            zs = [i] * len(group)
            ax.bar3d(xs, ys, zs, 0.4, 0.4, 0.4, color=color, alpha=0.6)
            for x, y, z, ball in zip(xs, ys, zs, group):
                ax.text(x, y, z, f'B{ball}', color='k', ha='center', va='bottom')

        plt.pause(1.5)

    plt.show()


if __name__ == "__main__":
    # Example setup: ball 5 is lighter
    balls = [1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1]

    odd_ball, odd_weight, steps = findOddBall(balls)
    print(f"The odd ball is ball {odd_ball} and it is {odd_weight}")
    visualize(steps)
