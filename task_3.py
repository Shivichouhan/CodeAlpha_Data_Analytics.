{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "df = sns.load_dataset('tips')\n",
    "sns.barplot(x='day', y='total_bill', data=df)\n",
    "plt.show()\n",
    "sns.scatterplot(x='total_bill', y='tip', data=df)\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "language_info": { "name": "python" }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
