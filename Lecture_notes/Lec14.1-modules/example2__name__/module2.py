import numpy as np 

def trigonometric_identity(angle: float) -> float:
    """Calculates the trigonometric identity 

        param: 
        angle: angle in radians

        return: trigonometric one
    """
    print("Running trigonometric_identity()")
    return np.cos(angle)**2 + np.sin(angle)**2

if __name__ == "__main__":
    print("Running directly from module2.py")
    print(f"{trigonometric_identity(np.pi)=}")
else:
    print("You are importing me")