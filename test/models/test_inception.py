from unittest import TestCase


class TestInception(TestCase):
    def test_forward(self):
        import torch
        from torch.autograd import Variable
        from reid.models.inception import Inception

        model = Inception(num_classes=5, num_features=256, dropout=0.5)
        x = Variable(torch.randn(10, 3, 144, 56), requires_grad=False)
        y = model(x)
        self.assertEquals(y.size(), (10, 5))

        model = Inception(num_features=8, dropout=0.5)
        x = Variable(torch.randn(10, 3, 144, 56), requires_grad=False)
        y = model(x)
        self.assertEquals(y.size(), (10, 8))
