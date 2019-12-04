#! /bin/bash
file=~/.oci/config
while IFS='=' read key value line
do
  echo $key
  echo $value
  sed -i "s#@$key#$value#g" "$CI_PROJECT_DIR"/ansible/test/integration/cloud-config-oci.yml
done < "$file"
