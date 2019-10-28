from fdfs_client.client import Fdfs_client, get_tracker_conf

try:
	tracker_path = get_tracker_conf('E:/×××/client.conf')  # 绝对路径
	client = Fdfs_client(tracker_path)

	# ret_upload
	upload_file_path = "E:/×××/img/0146000027.jpg"
	ret_upload = client.upload_by_filename(upload_file_path)
	print(ret_upload)

	# download
	local_filename = ""
	remote_file_id = ""
	ret_download = client.download_to_file(local_filename, remote_file_id)
	print(ret_download)

	# delete 注:file_id为bytes类型
	file_id = ret_upload['Remote file_id']
	ret_delete = client.delete_file(file_id)
	print(ret_delete)
except Exception as e:
	print('连接失败', e)
