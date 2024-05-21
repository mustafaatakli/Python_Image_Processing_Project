from PIL import Image
import numpy as np

#resmin adresini tanıtıp yüklenmei
resim = Image.open(r'C:\Users\matak\OneDrive\Masaüstü\task1\red_rose.jpg')
resim = resim.convert('RGB')

data = np.array(resim)

#gulun renk tanimi
gul_katmani = (data[:, :, 0] > 155) & (data[:, :, 1] < 85) & (data[:, :, 2] < 85)

#gul üzerineki mor rengin ve arkaplanın renk yogunlugunun ayarlanmasi
data[gul_katmani] = [200, 0, 200]
data[~gul_katmani] = [0, 0, 0]

#gulun yeni halinin kaydedilmesi
yeni_resim = Image.fromarray(data)
yeni_resim.save('purple_rose.jpg')

