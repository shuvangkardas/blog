![Confusion Matrix,Image Source Reference 1](/assets/images/Confusion-Matrix-Fun-Example.png)

Every time I read about these four terms i.e. True Positive(TP), True Negative(TN), False Positive(FP), and False Negative, I thought that I got it. Later I get confused and mess up. I guess this happens with you too. Maybe this is the reason these four terms are called confusion matrix or Error Matrix. 

After Googling these terms I came into this medium blog[^1] of Sarang Narkhede. The picture is convincing, still, I am not sure about remembering these terms. For remembering things, I always believe in connection. Connection is the best way to store things for the long term. If you read the book [[How to Take Smart Notes]] by Sönke Ahrens, you will get a good example of remembering the difference between artery and vein by creating connection with old knowledge. That's my favorite example. Ok! lot of pep talk. Let's come to the point. 

The confusion matrix is a table of 4 different combinations of predicted and actual values[^1]. All these terms consist of two words. The first part consists of True/False and the second part Positive/Negative.
You need to remember two connections to understand the confusion matrix:
1. **Second part(Positive/Negative) is the predicted value. That comes from your model or test**
2. **First part(True/False) verifies the second part. Whether the second part(prediction) is true or false.**


Consider a hypothetical scenario. A pregnancy test was done on urine samples of a man and woman. The woman is pregnant. Also, look into the picture. 
- **True Positive:** The prediction is **Positive**(women pregnant) that is **True**
- **True Negative:** The prediction is **Negative**(man not pregnant) that is **True**

This time the nurse forgetfully swapped the urine sample of the pregnant woman with a man :p 
- **False Positive:** The prediction is **Positive**(man pregnant) that is **False** and impossible!
- **False Negative:** The prediction is **Negative**(Women not pregnant) that is **False**

Now Read the two rules again. You will remember the confusion matrix for life. 

---
Shuvangkar Das, Potsdam, New York

Connect with me:
Twitter: [https://twitter.com/shuvangkar_das](https://twitter.com/shuvangkar_das)
LinkedIn: [https://www.linkedin.com/in/ShuvangkarDas/](https://www.linkedin.com/in/ShuvangkarDas)
YouTube: [https://www.youtube.com/ShuvangkarDas](https://www.youtube.com/ShuvangkarDas)

## References
[^1]: https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62