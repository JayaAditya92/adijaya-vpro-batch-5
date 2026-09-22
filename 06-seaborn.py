# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # tips = sns.load_dataset("tips")
# # sns.lineplot(data=tips, x="size", y="total_bill")
# # plt.show()

# # Ex2:scatterplot

# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # tips = sns.load_dataset("tips")
# # sns.scatterplot(data=tips, x="size", y="tip",hue="sex")
# # plt.show()

# # # Ex3: Barplot

# # from numpy import histogram
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # tips = sns.load_dataset("tips")
# # sns.barplot(data=tips, x="sex", y="tip")
# # plt.show()

# # Ex:histogram

# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # tips = sns.load_dataset("tips")
# # sns.histplot(tips["total_bill"],bins=20,kde=False)
# # plt.show()

# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # tips = sns.load_dataset("tips")
# # sns.histplot(tips["total_bill"],bins=20,kde=False)
# # plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt

# flights = sns.load_dataset("flights")
# print(flights.head(10))
# pivot = flights.pivot(index="month",columns="year",values="passengers")
# sns.heatmap(pivot,annot=True,fmt="d",cmap="plasma")
# plt.show()
