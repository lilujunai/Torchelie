import torch

from torchelie.nn import *


def test_adain():
    m = AdaIN2d(16, 8)
    m(torch.randn(5, 16, 8, 8), torch.randn(5, 8))


def test_film():
    m = FiLM2d(16, 8)
    m(torch.randn(5, 16, 8, 8), torch.randn(5, 8))


def test_bn():
    for M in [NoAffineBN2d, NoAffineMABN2d, BatchNorm2d, MovingAverageBN2d]:
        m = M(16)
        m(torch.randn(5, 16, 8, 8))

    for M in [ConditionalBN2d, ConditionalMABN2d]:
        m = M(16, 8)
        m(torch.randn(5, 16, 8, 8), torch.randn(5, 8))

    m = PixelNorm()
    m(torch.randn(5, 16, 8, 8))

    m = Lambda(lambda x: x + 1)
    m(torch.zeros(1))


def test_spade():
    for M in [Spade2d, SpadeMA2d]:
        m = M(16, 8, 4)
        m(torch.randn(5, 16, 8, 8), torch.randn(5, 8, 8, 8))


def test_attnnorm():
    m = AttenNorm2d(16, 8)
    m(torch.randn(1, 16, 8, 8))


def test_blocks():
    m = Conv2dNormReLU(4, 8, 3, nn.BatchNorm2d)
    m(torch.randn(1, 4, 8, 8))

    m = MConvNormReLU(4, 8, 3, nn.BatchNorm2d)
    m(torch.randn(1, 4, 8, 8))

    m = MConvBNrelu(4, 8, 3)
    m(torch.randn(1, 4, 8, 8))

    m = Conv2dBNReLU(4, 8, 3)
    m(torch.randn(1, 4, 8, 8))

    m = ResBlock(4, 8, 1)
    m(torch.randn(1, 4, 8, 8))

    m = PreactResBlock(4, 8, 1)
    m(torch.randn(1, 4, 8, 8))

    m = ConditionalResBlock(4, 8, 3, 1)
    m(torch.randn(1, 4, 8, 8), torch.randn(1, 3))

    m = SpadeResBlock(4, 4, 3, 1)
    m(torch.randn(1, 4, 8, 8), torch.randn(1, 3, 8, 8))

    m = SpadeResBlock(4, 8, 3, 1)
    m(torch.randn(1, 4, 8, 8), torch.randn(1, 3, 8, 8))

    m = AutoGANGenBlock(6, 3, [])
    m(torch.randn(1, 6, 8, 8))

    m = AutoGANGenBlock(3, 3, [])
    m(torch.randn(1, 3, 8, 8))

    m = AutoGANGenBlock(3, 3, [5])
    m(torch.randn(1, 3, 8, 8), [torch.randn(1, 5, 4, 4)])

def test_vq():
    m = VQ(8, 16, mode='nearest')
    m(torch.randn(10, 8))

    m = VQ(8, 16, mode='angular')
    m(torch.randn(10, 8))

    m = VQ(8, 16, mode='nearest', init_mode='first')
    m(torch.randn(10, 8))

    m = VQ(8, 16, mode='angular', init_mode='first')
    m(torch.randn(10, 8))


def test_tfms():
    m = ImageNetInputNorm()
    m(torch.randn(1, 3, 8, 8))


def test_maskedconv():
    m = MaskedConv2d(3, 8, 3, center=True)
    m(torch.randn(1, 3, 8, 8))
    m = TopLeftConv2d(3, 8, 3, center=True)
    m(torch.randn(1, 3, 8, 8))


def test_misc():
    m = Noise(1)
    m(torch.randn(1, 3, 8, 8))

    m = Debug('test')
    m(torch.randn(1, 3, 8, 8))

    m = Reshape(16)
    m(torch.randn(1, 4, 4))
