import os
import zipfile
from datetime import datetime
import argparse

class BackupManager:

    @staticmethod
    def zip_folder(src_path, output_folder):
        current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
        zip_file = os.path.join(output_folder, f"backup-{current_time}.zip")
        
        with zipfile.ZipFile(zip_file,"w",zipfile.ZIP_DEFLATED) as zipf:
            if os.path.isfile(src_path):
                zipf.write(src_path,os.path.basename(src_path))
            else:
                for root, _, files in os.walk(src_path):
                    for file in files:
                        file_path = os.path.join(root,file)
                        zipf.write(file_path,os.path.relpath(file_path,src_path))
                        
        print(f"backup complete: {zip_file}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple backup tool")
    parser.add_argument("source", help="File or folder to backup")
    parser.add_argument("output", help="Destination folder for the backup zip")
    args= parser.parse_args()
    
    BackupManager.zip_folder(args.source, args.output)