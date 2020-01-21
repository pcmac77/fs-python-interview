###########
# File Downloader
# Write a function to download a list of files.

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# !!!!! IMPORTANT !!!!!
# If it takes 1 second to download 1 file, it shouldn't 
#   take 10 seconds to download 10 files.
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# +++ START YOUR IMPLEMENTATION
def download(urls, dest_folder):
  """Download a collection of files designated by `urls` and save them
  in `dest_folder`.
  """
  pass
# --- START YOUR IMPLEMENTATION
  


def main():
  import time
  base_url = 'https://www.grc.com/sn/'
  urls = []
  start = time.time()
  for i in range(500, 511):
    # urls.append(base_url + 'SN-' + str(i) + '-notes.pdf')
    urls.append(f'{base_url}SN-{i}-notes.pdf')
  download(urls, ".")
  end = time.time()
  print(f'Total time taken: {end-start:.2f}')

main()
print("---Done with file_downloader")
