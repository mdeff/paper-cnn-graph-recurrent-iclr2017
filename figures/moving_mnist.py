import matplotlib.pyplot as plt

conv1_5x5 = [5579, 5263, 4847, 4601, 4419, 4400, 4287, 4215, 4120, 4171, 3982, 4003, 3951]
gconv1_K3 = [5718, 5482, 5350, 5243, 5082, 4822, 4729, 4662, 4567, 4526, 4438, 4371, 4347, 4391, 4299, 4221, 4276, 4204, 4232, 4162, 4167]
gconv1_K5 = [5367, 4731, 4435, 4305, 4108, 4057, 3933, 3865, 3836, 3830, 3741, 3770, 3701, 3731, 3659, 3725, 3641, 3594, 3612]
gconv1_K7 = [5080, 4594, 4266, 4149, 3983, 3858, 3801, 3736, 3727]

plt.figure(figsize=(15,5))
plt.plot(range(1,len(conv1_5x5)+1), conv1_5x5, '.-', markersize=12, label='LSTM+CNN, 5x5 filters')
plt.plot(range(1,len(gconv1_K3)+1), gconv1_K3, '.-', markersize=12, label='LSTM+GCNN, K=3')
plt.plot(range(1,len(gconv1_K5)+1), gconv1_K5, '.-', markersize=12, label='LSTM+GCNN, K=5')
plt.plot(range(1,len(gconv1_K7)+1), gconv1_K7, '.-', markersize=12, label='LSTM+GCNN, K=7')
plt.legend()
plt.xlabel('#epoch')
plt.ylabel('validation cross-entropy')
plt.savefig('moving_mnist.pdf')
