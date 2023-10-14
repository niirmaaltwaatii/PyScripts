import os
import shutil

def organize_files(directory):
    # Define the subdirectory names
    subdirectories = ['images', 'audios', 'videos', 'documents', 'others']

    # Create the subdirectories if they don't exist
    for subdirectory in subdirectories:
        os.makedirs(os.path.join(directory, subdirectory), exist_ok=True)

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for filename in files:
            source_path = os.path.join(root, filename)

            # Determine the file type
            file_extension = filename.split('.')[-1].lower()
            if file_extension in ('jpg', 'jpeg', 'png', 'gif'):
                destination = os.path.join(directory, 'images')
            elif file_extension in ('mp3', 'wav'):
                destination = os.path.join(directory, 'audios')
            elif file_extension in ('mp4', 'avi', 'mkv'):
                destination = os.path.join(directory, 'videos')
            elif file_extension in ('pdf', 'doc', 'docx', 'txt'):
                destination = os.path.join(directory, 'documents')
            else:
                destination = os.path.join(directory, 'others')

            # Move the file to its respective directory
            shutil.move(source_path, os.path.join(destination, filename))

    # Remove empty directories
    for root, dirs, _ in os.walk(directory, topdown=False):
        for subdir in dirs:
            current_dir = os.path.join(root, subdir)
            if not os.listdir(current_dir):
                os.rmdir(current_dir)

if __name__ == "__main__":
    target_directory = input("Enter the directory path to organize: ")
    organize_files(target_directory)
    print("Files organized and empty directories deleted successfully.")
