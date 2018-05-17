#!/bin/bash
backdate=`date +%Y%m%d%H%M%S`
backpath=/backup/xiajl.cn/
filepath=/data/xiajl.cn/
backdb=(solo)

#mkdir directory
if [ ! -d $backpath ]; then
    mkdir -p $backpath
fi

for db in ${backdb[@]}
do
  backfile=$backpath"/"$db"."$backdate".sql"
  rm -rf $backfile".gz"
  mysqldump  -hlocalhost -uroot -P12591 -p10GsKranPNS@FNOins-m   --skip-lock-tables   --default-character-set=utf8  $db>$backfile
  gzip $backfile
  # 复制最新数据库文件，以便备份
  rm -rf $backpath/$db.latest.gz
  cp $backfile".gz" $backpath/$db.latest.gz
done

# 备份图片等上传的资源
rm -rf $backpath"xiajl.cn.tar.gz"
cd $backpath
tar -czf xiajl.cn.tar.gz $filepath

#clear 30 days ago
find $backpath -mtime +30 -exec rm -rf {} \;