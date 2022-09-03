import zipfile

# Zipping
comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# # unzipping
# zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
# zip_obj.extractall('extract_path')

# zipping entire directory
# import shutil
#
#
# dir_to_zip = "give absolute path"
# output_file = 'give where to unzip'
# shutil.make_archive(output_file, 'zip', dir_to_zip)
