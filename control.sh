#!/bin/bash

APPHOME=`dirname "$0"`
APPHOME=`cd "$APPHOME"; pwd`

echo "run at "$APPHOME
bin/imageteller.sh -d $APPHOME $1
