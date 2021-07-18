chmod 1777 /tmp
pip3 install pyaml
pip3 install sentencepiece
pip3 install sox
pip3 install typeguard
pip3 install tensorboardX
pip3 install torch==1.7.0 torchvision==0.8.1 torchaudio==0.7.1 -f https://download.pytorch.org/whl/cu101/torch_stable.html


# download data
dbase=/opt/tiger/speech_data
if [ ! -d $dbase ]; then
    mkdir -p $dbase
fi

aishell_url=https://openslr.magicdatatech.com/resources/33
thchs_url=https://openslr.magicdatatech.com/resources/18
aidatatang_url=www.openslr.org/resources/62
magicdata_url=www.openslr.org/resources/68
primewords_url=www.openslr.org/resources/47
stcmds_url=www.openslr.org/resources/38

sh ./cn_demo/multi_cn/local/aishell_download_and_untar.sh $dbase/aishell $aishell_url data_aishell || exit 1;
sh ./cn_demo/multi_cn/local/thchs_download_and_untar.sh $dbase/thchs $thchs_url data_thchs30 || exit 1;