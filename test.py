from PIL import Image
import numpy as np
from vifvec import vifvec
import sys

a = sys.argv[1]
b = sys.argv[2]
sigmasq = float(sys.argv[3])
M = int(sys.argv[4])

#Load reference image
imref = np.array(Image.open(a).convert('L')).astype(float)

# Load distorted image
imdist = np.array(Image.open(b).convert('L')).astype(float)

#Calculate VIF score

vif_score = vifvec(imref, imdist, sigmasq, M)
print(float(vif_score[0]))
