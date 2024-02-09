#!/usr/bin/bash

cleaning_all_images()
{
  read -p "This operation will remove all the current container iamges. Proceed? (y/n): " answer

  if [ "$answer" == "y" ]; then
    echo "Ok, proceeding and removing all the local images"
  else
    echo "exiting ..."
    exit 1
  fi
  podman rmi -a --force
}

check_final_dir()
{
  if [ -d /tmp/app ]; then
    echo "The directory '/tmp/app' is present, removing it"
    echo "running the command 'rm -rfv /tmp/app/'"
    rm -rfv /tmp/app/
  fi

  mkdir -pv /tmp/app
}

create_py38_container()
{
  # Creating the container
  podman build . -t py_38 -f Containerfile.py_38 --layers=false --no-cache
}

create_crhc-cli_container()
{
  # Creating the container
  podman build . -t crhc-pkg -f Containerfile.crhc-pkg --layers=false --no-cache
}

create_crhc_bin()
{
  # Running the container and creating the binary at /tmp/app
  podman run --rm --name crhc-cli-build -v /tmp/app:/app:Z localhost/crhc-pkg
}

# Main
cleaning_all_images
check_final_dir
create_py38_container
create_crhc-cli_container
create_crhc_bin
