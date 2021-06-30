import torch
import torch.nn as nn

from module.vgg import VGG2L
from module.ctc.ctc import CTC_Module

class CNN_CTC(nn.Module):
    def __init__(self, conf) -> None:
        super().__init__()
        self.encoder = VGG2L(conf.idim, conf.odim, conf.pos_enc)
        self.CTC_Module = CTC_Module(conf.odim, conf.encoder_output_size, dropout_rate=0.2, reduce= True)

    def forward(self, x, x_len, targets, targets_len):
        cnn_x, _ , cnn_x_len = self.encoder(x, x_len, mask=None)
        return self.ctc_loss(cnn_x, cnn_x_len, targets, targets_len)

    def ctc_loss(self, inputs, inputs_len, targets, target_len):
        loss = self.CTC_Module(inputs, inputs_len, targets, target_len)
        return loss