import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.random.randint(1, 10, 10)
karesi = x * x
kup = x * x * x
print(x)

plt.subplot(2, 1, 1)
plt.plot(karesi, "r--") #red rengin kısaltması "r" dir
plt.title("x'in karesi")

plt.subplot(2, 1, 2)
plt.plot(kup, "g--") #green rengin kısaltması "g" dir
plt.title("x'in küpü")
plt.tight_layout()
plt.show()

veri = pd.DataFrame({
    "0-1 random": np.random.rand(20), #Untuma randint'in kısaltması rand dır.
    "1-100 randint": np.random.randint(1, 10, 20),
    "ones": np.ones(20),
    "arange": np.arange(50, 70)
})

print(veri)

veri["yeni_sutun"] = veri["1-100 randint"] + veri["arange"]
print(veri)
