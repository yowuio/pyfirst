import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建图形
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# 定义节点位置
nodes = {
    'A': (1, 6, '你的缺陷'),
    'B': (3, 6, '顶撞领导/拖延汇报'),
    'C': (5, 6, '但具备'),
    'D': (2, 4, '攻克技术壁垒能力'),
    'E': (4, 4, '搞定难缠客户资源'),
    'F': (6, 4, '历史救火功臣身份'),
    'G': (7, 2, '留你收益>优化成本')
}

# 绘制节点
for key, (x, y, text) in nodes.items():
    if key == 'C':
        # 菱形节点
        diamond = patches.Polygon([(x-0.5, y), (x, y+0.5), (x+0.5, y), (x, y-0.5)], 
                                 facecolor='lightblue', edgecolor='black', linewidth=2)
        ax.add_patch(diamond)
    else:
        # 矩形节点
        rect = FancyBboxPatch((x-0.8, y-0.3), 1.6, 0.6, 
                             boxstyle="round,pad=0.1", 
                             facecolor='lightgreen', edgecolor='black', linewidth=2)
        ax.add_patch(rect)
    
    ax.text(x, y, text, ha='center', va='center', fontsize=10, weight='bold')

# 绘制连接线
connections = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('C', 'E'),
    ('C', 'F'),
    ('F', 'G')
]

for start, end in connections:
    x1, y1, _ = nodes[start]
    x2, y2, _ = nodes[end]
    
    # 调整连接点位置
    if start == 'C' and end in ['D', 'E', 'F']:
        # 从菱形到矩形的连接
        if end == 'D':
            start_point = (x1-0.3, y1-0.3)
        elif end == 'E':
            start_point = (x1, y1-0.5)
        else:  # F
            start_point = (x1+0.3, y1-0.3)
        end_point = (x2, y2+0.3)
    elif start == 'F' and end == 'G':
        start_point = (x1, y1-0.3)
        end_point = (x2, y2+0.3)
    else:
        start_point = (x1+0.8, y1)
        end_point = (x2-0.8, y2)
    
    arrow = ConnectionPatch(start_point, end_point, "data", "data",
                          arrowstyle="->", shrinkA=5, shrinkB=5,
                          mutation_scale=20, fc="black", lw=2)
    ax.add_patch(arrow)

plt.title('流程图', fontsize=16, weight='bold', pad=20)
plt.tight_layout()
plt.savefig('flowchart.png', dpi=300, bbox_inches='tight')
plt.show()

print("图表已生成并保存为 flowchart.png") 