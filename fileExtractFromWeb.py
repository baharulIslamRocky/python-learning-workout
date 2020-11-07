import os
import tarfile
from six.moves import urllib


destinationDirectory='august/saturday'
sourceDirectory='G:\MINE\SUB\TERM__-4\T4_Level_3\ISM\Final\ImportTest\housing.tgz'
if not os.path.isdir(destinationDirectory):
    os.makedirs(destinationDirectory)
tgzPath=os.path.join(destinationDirectory,'hous.tgz')
urllib.request.urlretrieve(sourceDirectory,tgzPath)

tgzfile=tarfile.open(tgzPath)
tgzfile.extractall(path=destinationDirectory)
tgzfile.close()

import pandas as pd
load=pd.read_csv((destinationDirectory+'/housing.csv'))
print(load.head())
                     
