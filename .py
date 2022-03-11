import numpy as np

def calculate(num_list):
    if len(num_list) != 9:
        print('ERROR : List must contain nine numbers')
    else:
        array=np.array(num_list)
        matrix= array.reshape(3,3)
        
        calculations={
            'mean':[matrix.mean(axis=1).tolist(),matrix.mean(axis=0).tolist(),array.mean()] ,
            'variance':[matrix.var(axis=1).tolist(),matrix.var(axis=0).tolist(),array.var()] ,
            'standard deviation':[matrix.std(axis=1).tolist(),matrix.std(axis=0).tolist(),array.std()] ,
            'max': [matrix.max(axis=1).tolist(),matrix.max(axis=0).tolist(),array.max()],
            'min': [matrix.min(axis=1).tolist(),matrix.min(axis=0).tolist(),array.min()],
            'sum': [matrix.sum(axis=1).tolist(),matrix.sum(axis=0).tolist(),array.sum()]
        }
        
    return calculations
calculate([1,2,3,4,5,6,7,8,9])
