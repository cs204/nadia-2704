fileName = input('File name: ')
extension = fileName.split('.')[-1]
match extension:
    case 'jpg' | 'jpeg': print('image/jpeg')
    case 'png': print('image/png')
    case 'pdf': print('application/pdf')
    case 'txt': print('text/plain')
    case 'zip': print('application/zip')
    case _: print('application/octet-stream')