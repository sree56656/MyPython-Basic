# !/bin/bash
echo 'Setup and Configure Server'
file_name = $2
config_files =$1
if [-d 'config']
then
  echo "reading config directory"
  config_files = $(ls config)
else
  echo 'creating config directory'
  mkdir config
fi
echo "using $file_name to configure something"
echo "here are all configuration files : $config_files"