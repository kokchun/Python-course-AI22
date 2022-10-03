import matplotlib.pyplot as plt 

class PlotVectors:
    def __init__(self, *vectors) -> None:
        X, Y = [], []
    
        for vector in vectors:            
            X.append(vector[0])
            Y.append(vector[1])

        self.X, self.Y = X, Y
        self.originX = self.originY = tuple(0 for _ in range(len(X)))

    def plot(self) -> None:
        """ Visualize vectors """
        plt.quiver(self.originX, self.originY, self.X, self.Y, scale=1,
                scale_units="xy", angles="xy")
        plt.xlim(-2, 10)
        plt.ylim(-2, 10)
        plt.xlabel("x")
        plt.ylabel("y")
        title = " ".join(f"{X, Y}" for X,Y in zip(self.X, self.Y))
        plt.title(f"Vectors: {title}")
        plt.grid()
        plt.show()

