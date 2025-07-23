# import numpy as np
# import pandas as pd
# import torch
# from notears.linear import notears_linear
# from notears.nonlinear import notears_nonlinear, NotearsMLP

# def run_notears(data, is_categorical=False):
#     """
#     非线性 NOTEARS 算法（支持数值型和类别型特征）
#     :param data: 输入数据（数值型或已处理的类别型）
#     :param is_categorical: 是否为类别型特征（影响模型结构）
#     """
#     # 定义模型结构（移除 dtype 参数）
#     if is_categorical:
#         # 对类别型特征使用嵌入层（Embedding）
#         model = NotearsMLP(
#             dims=[data.shape[1], 10, 1],  # 输入维度 -> 隐藏层 -> 输出层
#             bias=True
#         )
#     else:
#         # 数值型特征使用默认结构
#         model = NotearsMLP(
#             dims=[data.shape[1], 10, 1],
#             bias=True
#         )
    
#     # 确保模型权重为 float32
#     model = model.float()  # 显式转换模型参数类型
    
#     # 调用非线性 NOTEARS 算法
#     A = notears_nonlinear(
#         X=data.values,
#         lambda1=0.01,  # L1正则化（控制稀疏性）
#         lambda2=0.01,  # L2正则化（防止过拟合）
#         max_iter=50,
#         model=model
#     )
#     return A

# def extract_causal_mask(data, is_categorical=False):
#     """
#     提取因果图（支持数值型和类别型特征）
#     :param data: 输入数据（Pandas DataFrame）
#     :param is_categorical: 是否为类别型特征
#     """
#     # 强制转换数据类型为 float32
#     data = data.astype(np.float32)
    
#     print("Running Nonlinear NOTEARS algorithm...")
#     notears_matrix = run_notears(data, is_categorical=is_categorical)
    
#     # 打印结果
#     print("\nNOTEARS algorithm result:")
#     print(notears_matrix)
    
#     # 转换为二值因果图（调整阈值）
#     causal_graph = (np.abs(notears_matrix) > 0.3).astype(int)
    
#     print("\nFinal causal graph:")
#     print(causal_graph)
    
#     return causal_graph
import numpy as np
import pandas as pd
import torch
from notears.linear import notears_linear
from notears.nonlinear import notears_nonlinear, NotearsMLP

def run_notears(data, linear=False, is_categorical=False):
    """
    NOTEARS 算法（支持线性/非线性，数值型和类别型特征）
    :param data: 输入数据（数值型或已处理的类别型）
    :param linear: 是否使用线性模型（True）或非线性模型（False）
    :param is_categorical: 是否为类别型特征（仅影响非线性模型结构）
    """
    if linear:
        print("Using linear NOTEARS model")
        # 线性模型直接调用notears_linear
        A = notears_linear(
            X=data.values,
            lambda1=0.01,       # L1正则化（控制稀疏性）
            loss_type='l2',     # 使用L2损失
            max_iter=50
        )
    else:
        print("Using nonlinear NOTEARS model")
        # 非线性模型保持原有逻辑
        if is_categorical:
            # 对类别型特征使用嵌入层（Embedding）
            model = NotearsMLP(
                dims=[data.shape[1], 10, 1],  # 输入维度 -> 隐藏层 -> 输出层
                bias=True
            )
        else:
            # 数值型特征使用默认结构
            model = NotearsMLP(
                dims=[data.shape[1], 10, 1],
                bias=True
            )
        
        # 确保模型权重为 float32
        model = model.half()
        
        # 调用非线性 NOTEARS 算法
        A = notears_nonlinear(
            X=data.values,
            lambda1=0.01,   # L1正则化（控制稀疏性）
            lambda2=0.01,   # L2正则化（防止过拟合）
            max_iter=50,
            model=model
        )
    return A

def extract_causal_mask(data, is_categorical=False, linear=False):
    """
    提取因果图（支持数值型和类别型特征）
    :param data: 输入数据（Pandas DataFrame）
    :param is_categorical: 是否为类别型特征（影响非线性模型结构）
    :param linear: 是否使用线性模型（True）或非线性模型（False）
    """
    # 强制转换数据类型为 float32
    data = data.astype(np.float32)
    
    # 根据模型类型输出提示
    model_type = "Linear" if linear else "Nonlinear"
    print(f"Running {model_type} NOTEARS algorithm...")
    
    # 调用NOTEARS算法
    notears_matrix = run_notears(
        data=data,
        linear=linear,
        is_categorical=is_categorical
    )
    
    # 打印结果
    print("\nNOTEARS algorithm result:")
    print(notears_matrix)
    
    # 转换为二值因果图（调整阈值）
    causal_graph = (np.abs(notears_matrix) > 0.1).astype(int)
    
    print("\nFinal causal graph:")
    print(causal_graph)
    
    return causal_graph