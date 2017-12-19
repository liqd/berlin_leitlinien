#!/bin/sh

set -e -v

if [ -n ${TRAVIS_SSH_SECRET} ]; then
    SSH_ID_ARG="-i ${HOME}/id_rsa"
    cat <<EOF | openssl enc -d -pass env:TRAVIS_SSH_SECRET -aes256 -a -out ~/id_rsa
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
ZZt+mFZkrg/cjRBt39NWGw==
EOF
    chmod 600 ~/id_rsa
fi

ssh -p 22036 ${SSH_ID_ARG} -oStrictHostKeyChecking=no build@benhabib.liqd.net deploy berlin-leitlinien master
