class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def solution(numbers, target):
    root = TreeNode(0)
    current_level = [root]
    for number in numbers:
        next_level = []

        for node in current_level:
            node.left = TreeNode(node.value + number)
            node.right = TreeNode(node.value - number)

            next_level.append(node.left)
            next_level.append(node.right)
        current_level = next_level
        
    return sum(1 for node in current_level if node.value == target)

def solution2(numbers, target):
    current_level = [0]
    for number in numbers:
        next_level = []

        for node in current_level:
            next_level.append(node + number)
            next_level.append(node - number)
        current_level = next_level
    return sum(1 for node in current_level if node == target)

numbers1 = [1, 1, 1, 1, 1]
target1 = 3
numbers2 = [4, 1, 2, 1]
target2 = 4

print(solution(numbers1, target1)) # 5
print(solution(numbers2, target2)) # 2
print(solution2(numbers1, target1)) # 5
print(solution2(numbers2, target2)) # 2

