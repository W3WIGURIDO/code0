from PIL import Image
import os
import pickle

class Cifar100:
    topdirname = 'cifar-100-python'
    width, height = 32, 32
    def __init__(self, extractedpath):
        dirpath = os.path.join(extractedpath, Cifar100.topdirname)
        with open(os.path.join(dirpath, 'meta'), 'rb') as fp:
            self.meta = pickle.load(fp)
            self.fine_label_names = self.meta['fine_label_names']
            self.coarse_label_names = self.meta['coarse_label_names']
        with open(os.path.join(dirpath, 'train'), 'rb') as fp:
            self.train = pickle.load(fp)
        with open(os.path.join(dirpath, 'test'), 'rb') as fp:
            self.test = pickle.load(fp)

    def _out_images(self, path, data, filename, coarse, fine):
        for (d, f, cl, fl) in zip(data, filename, coarse, fine):
            im = Image.new('RGB', (Cifar100.width, Cifar100.height), (0xff, 0xff, 0xff))
            putdata = []
            for wh in range(Cifar100.width * Cifar100.height):
                r = d[wh]
                g = d[wh + Cifar100.width * Cifar100.height]
                b = d[wh + 2 * Cifar100.width * Cifar100.height]
                putdata.append((r, g, b))
            im.putdata(putdata)
            super_class = cifar.coarse_label_names[cl]
            sub_class = cifar.fine_label_names[fl]
            if not os.path.isdir(path + "/" + super_class):
                os.mkdir(path + "/" + super_class)
            if not os.path.isdir(path + "/" + super_class + "/" + sub_class):
                os.mkdir(path + "/" + super_class + "/" + sub_class)
            im.save(os.path.join(path + "/" + super_class + "/" + sub_class, f))
            print(os.path.join(path + "/" + super_class + "/" + sub_class, f))

    def out_images(self, path):
        trainpath = os.path.join(path, 'train')
        if not os.path.isdir(trainpath):
            os.mkdir(trainpath)
        self._out_images(trainpath, self.train['data'], self.train['filenames'], self.train['coarse_labels'], self.train['fine_labels'])
        testpath = os.path.join(path, 'test')
        if not os.path.isdir(testpath):
            os.mkdir(testpath)
        self._out_images(testpath, self.test['data'], self.test['filenames'], self.test['coarse_labels'], self.test['fine_labels'])

if __name__ == '__main__':
    cifar = Cifar100('./')
    cifar.out_images('./data')