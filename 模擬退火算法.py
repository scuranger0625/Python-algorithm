import math
import random

# 定義目標函數（需要最小化）
def objective_function(x):
    """
    目標函數：計算輸入 x 對應的函數值。
    在這裡，目標函數包含平方項和正弦、餘弦函數的組合。
    """
    return x**2 + 4*math.sin(5*x) + 2*math.cos(3*x)

# 模擬退火算法實現
def simulated_annealing():
    """
    模擬退火算法實現，用於尋找目標函數的最小值。
    """
    # 初始化參數
    current_solution = random.uniform(-10, 10)  # 隨機生成一個初始解，範圍在 [-10, 10]
    current_value = objective_function(current_solution)  # 計算初始解對應的目標函數值
    temperature = 100  # 初始溫度，控制接受次優解的概率
    cooling_rate = 0.95  # 降溫速率，每次迭代溫度乘以此值
    min_temperature = 1e-3  # 最低溫度，作為停止條件

    # 記錄全局最優解
    best_solution = current_solution  # 初始化全局最優解為當前解
    best_value = current_value  # 初始化全局最優值為當前目標函數值

    # 開始迭代過程
    while temperature > min_temperature:
        # 在當前解的鄰域內隨機生成一個新解
        # 鄰域是通過在當前解附近添加隨機偏移生成的
        new_solution = current_solution + random.uniform(-1, 1)
        new_value = objective_function(new_solution)  # 計算新解的目標函數值

        # 計算能量差，即目標函數值的變化
        delta = new_value - current_value

        # 決定是否接受新解
        if delta < 0:
            # 如果新解更優（目標函數值更小），直接接受新解
            current_solution = new_solution
            current_value = new_value
        else:
            # 如果新解不如當前解，以一定概率接受新解
            # 接受概率由指數函數 exp(-delta / temperature) 決定
            if random.random() < math.exp(-delta / temperature):
                current_solution = new_solution
                current_value = new_value

        # 更新全局最優解
        if current_value < best_value:
            # 如果當前解比已知的全局最優解更優，更新全局最優解
            best_solution = current_solution
            best_value = current_value

        # 降低溫度，按照 cooling_rate 遞減
        temperature *= cooling_rate

    # 返回全局最優解和對應的目標函數值
    return best_solution, best_value

# 運行模擬退火算法
best_solution, best_value = simulated_annealing()
print(f"最佳解: {best_solution}, 最小值: {best_value}")
