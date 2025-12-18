{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from textblob import TextBlob\n",
    "reviews = ['Great product!', 'Very bad service', 'It was okay']\n",
    "for r in reviews:\n",
    "    print(f'{r} -> {TextBlob(r).sentiment}')"
   ]
  }
 ],
 "metadata": {
  "language_info": { "name": "python" }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
