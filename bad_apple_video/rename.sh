sudo apt update

#rename utils
sudo apt install rename

ls -v bad_apple_image*.png | cat -n | while read n f; do mv "$f" "frame_$(printf "%04d" $n).png"; done
