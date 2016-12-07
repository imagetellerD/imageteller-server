#!/bin/bash

PNAME=omg-imageteller
VERSION=0.1.0

rm -rf target
mkdir target

SCRATCH_DIR="$PNAME-$VERSION"

cd target
mkdir $SCRATCH_DIR

# 在这里将需要发布的文件，放到scratch目录下
cp -r ../lib ../bin ../conf $SCRATCH_DIR
sed -i -e "s/__BUILD_VERSION__/$VERSION/" $SCRATCH_DIR/bin/imageteller.sh
find $SCRATCH_DIR -name '*.sh' -exec chmod +x {} \;
find $SCRATCH_DIR -name '*.py' -exec chmod +x {} \;
chmod +x $SCRATCH_DIR/bin/*

# 添加log目录
mkdir $SCRATCH_DIR/log

# 删除svn目录
find -name '.svn' -exec rm -rf {} \; 2>/dev/null
find -name *~ -exec rm -rf {} \; 2>/dev/null

#tar czf $SCRATCH_DIR.tar.gz $SCRATCH_DIR
fpm -s dir -t rpm -n $PNAME -v $VERSION --epoch=`date +%s` --rpm-defattrfile=0755 --prefix=/usr/local/domob/prog.d $SCRATCH_DIR

RET=$?

# 其实就一个md5文件，只是为了简单得到文件名，用for来做
for file in *.rpm; do
	md5sum $file > $file.md5
done

rm -rf $SCRATCH_DIR

exit $RET
