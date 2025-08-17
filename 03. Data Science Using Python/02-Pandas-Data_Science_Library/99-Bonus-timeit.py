"""
This section is for checking time for above 2 Statmenets
"""
#### Section Start ####
import timeit
setup = """
import numpy as np
import pandas as pd
tipsdata = pd.read_csv("./Excel Files/tips.csv")
def quality(total_bill,tip):
    if tip/total_bill > 0.25:
        return "Generous"
    else:
        return "Other"
"""
stmt1 = """
tipsdata["tipquality"] = tipsdata[["total_bill","tip"]].apply(lambda tipsdata: quality(tipsdata["total_bill"],tipsdata["tip"]),axis=1)
"""
stmt2 = """
tipsdata["quality"] = np.vectorize(quality)(tipsdata["total_bill"],tipsdata["tip"])
"""

a = timeit.timeit(setup = setup,stmt=stmt1,number = 1000)
b = timeit.timeit(setup = setup,stmt=stmt2,number = 1000)

print("The First Method Took :",a)
print("The Second Method Took :",b)

### Section End ###