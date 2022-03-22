#!/bin/bash

# 
#  Developer .: Waldirio M Pinheiro <waldirio@gmail.com>/<waldirio@redhat.com>
#  Date ......: 11/07/2021
#  Purpose ...: End to End test to check the crhc-cli app
# 


CRHC="/tmp/crhc-cli/crhc.py"

#
# Please, create the file in your home directory called ".token" and with the content as below. Please,
# update the token properly.
#
# TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCIg..."
#

source ~/.token
DATE=$(date +%m-%d-%Y_%H:%M:%S)
LOG="/tmp/crhc-system-test_$DATE.log"
> $LOG

check_packages()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Checking for python3 package"													| tee -a $LOG
  check_python3=$(rpm -qa | grep ^python3 | wc -l)
  if [ $check_python3 == 0 ]; then
    echo "exiting ... please, install python3 package"																				| tee -a $LOG
    exit
  fi

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Checking for git package"															| tee -a $LOG
  check_python3=$(rpm -qa | grep ^git | wc -l)
  if [ $check_python3 == 0 ]; then
    echo "exiting ... please, install git package"																						| tee -a $LOG
    exit
  fi
}

virtualenv()
{
  if [ $2 == "" ]; then
    url="https://github.com/C-RH-C/crhc-cli.git"
  else
    url=$2
  fi

  if [ -d /tmp/crhc-cli ]; then
    echo "## $(date +%m-%d-%Y_%H:%M:%S) - Removing current /tmp/crhc-cli dir ..."							| tee -a $LOG
    rm -rf /tmp/crhc-cli																																			| tee -a $LOG
  fi

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Cloning the crhc-cli repository: $url"								| tee -a $LOG
  #url="https://github.com/C-RH-C/crhc-cli.git"
  cd /tmp
  if [ "$1" <> " " ]; then
    echo "## $(date +%m-%d-%Y_%H:%M:%S) - Cloning the crhc-cli repository from branch '$1'"		| tee -a $LOG
    git clone -b $1 $url
    if [ $? -ne 0 ]; then
      echo "something is wrong, probably the branch '$1' doesn't exist"
      echo "exiting ..."
      exit
    fi
  else
    echo "## $(date +%m-%d-%Y_%H:%M:%S) - Cloning the crhc-cli repository from origin"				| tee -a $LOG
    git clone $url																																						| tee -a $LOG
  fi
  cd crhc-cli


  if [ -d ~/.venv/crhc-cli ]; then
    echo "## $(date +%m-%d-%Y_%H:%M:%S) - Removing current venv dir ..."											| tee -a $LOG
    rm -rf ~/.venv/crhc-cli																																		| tee -a $LOG
  fi

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Creating the virtual env"															| tee -a $LOG
  python3 -m venv ~/.venv/crhc-cli																														| tee -a $LOG

  if [ -d ~/.venv/crhc-cli ]; then
    echo "## $(date +%m-%d-%Y_%H:%M:%S) - Virtual environment created successfully"						| tee -a $LOG
  fi

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Loading the Virtual Environment"											| tee -a $LOG
  source ~/.venv/crhc-cli/bin/activate

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Installing the requirements"													| tee -a $LOG
  ~/.venv/crhc-cli/bin/pip install --upgrade pip																							| tee -a $LOG
  ~/.venv/crhc-cli/bin/pip install -r requirements.txt																				| tee -a $LOG
}


inventory_def()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Inventory Pipeline"										| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - inventory menu"												| tee -a $LOG
  $CRHC inventory																															| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - inventory list"												| tee -a $LOG
  $CRHC inventory list 																												| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - inventory list_all"										| tee -a $LOG
  $CRHC inventory list_all 																										| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - inventory display_name"								| tee -a $LOG
  $CRHC inventory display_name	  																						| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - inventory list --csv"									| tee -a $LOG
  $CRHC inventory list --csv																									| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - inventory list_all --csv"							| tee -a $LOG
  $CRHC inventory list_all --csv																							| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - inventory display_name esxi1"					| tee -a $LOG
  $CRHC inventory display_name esxi1																					| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - inventory display_name esxi1 --csv"		| tee -a $LOG
  $CRHC inventory display_name esxi1 --csv																		| tee -a $LOG
}

swatch_def()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Swatch Pipeline"											| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - swatch menu"													| tee -a $LOG
  $CRHC swatch																																| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - swatch list"													| tee -a $LOG
  $CRHC swatch list 																													| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - swatch list_all"											| tee -a $LOG
  $CRHC swatch list_all																												| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - swatch list --csv"										| tee -a $LOG
  $CRHC swatch list --csv																											| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - swatch list_all --csv"								| tee -a $LOG
  $CRHC swatch list_all --csv																									| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - swatch socket_summary"								| tee -a $LOG
  $CRHC swatch socket_summary																									| tee -a $LOG
}

patch_def()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Patch Pipeline"	       								| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - patch"				         								| tee -a $LOG
  $CRHC patch 																																| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - patch systems"         								| tee -a $LOG
  $CRHC patch systems																													| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - patch systems --csv"   								| tee -a $LOG
  $CRHC patch systems	--csv																										| tee -a $LOG
}

vulnerability_def()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Vulnerability Pipeline"								| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - vulnerability"	       								| tee -a $LOG
  $CRHC vulnerability																													| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - vulnerability systems"  							| tee -a $LOG
  $CRHC vulnerability systems																									| tee -a $LOG
	
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - vulnerability systems --csv"					| tee -a $LOG
  $CRHC vulnerability systems	--csv																						| tee -a $LOG
}

advisor_def()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Advisor Pipeline"											| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - advisor"	 														| tee -a $LOG
  $CRHC advisor 																															| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - advisor systems"  										| tee -a $LOG
  $CRHC advisor systems 																											| tee -a $LOG
	
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - advisor systems --csv"								| tee -a $LOG
  $CRHC advisor systems	--csv 														 										| tee -a $LOG
}

ts_def()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Ts Pipeline"    											| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - ts menu"															| tee -a $LOG
  $CRHC ts																																		| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - ts dump"															| tee -a $LOG
  $CRHC ts dump																																| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - ts match"															| tee -a $LOG
  $CRHC ts match																															| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - ts match (files already in place)"		| tee -a $LOG
  $CRHC ts match																															| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - ts clean"															| tee -a $LOG
  $CRHC ts clean																															| tee -a $LOG
}


endpoint_def()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Endpoint Pipeline"										| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - endpoint list"												| tee -a $LOG
  $CRHC endpoint list																													| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - checking all the endpoint"						| tee -a $LOG
  for b in $($CRHC endpoint list | grep \" | cut -d\" -f2 | sed '1d'); do echo - $b; $CRHC get $b; echo; done 		| tee -a $LOG

  #$CRHC get <API ENDPOINT>
  #$CRHC get <API ENDPOINT>
  #$CRHC login --token <user api token here>
  #$CRHC logout
}

binary_def()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Bynary Pipeline"              				| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - generating the bynary version"				| tee -a $LOG
  ~/.venv/crhc-cli/bin/pyinstaller --onefile $CRHC 														| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - ldd binary file"											| tee -a $LOG
  ldd /tmp/crhc-cli/dist/crhc											 														| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - executing the binary file"						| tee -a $LOG
  /tmp/crhc-cli/dist/crhc											 																| tee -a $LOG
}

general_def()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - General Pipeline"											| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - token"																| tee -a $LOG
  $CRHC token																																	| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - whoami"																| tee -a $LOG
  $CRHC whoami																																| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - '--version'"													| tee -a $LOG
  $CRHC --version																															| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - '-v'"																	| tee -a $LOG
  $CRHC -v																																		| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - '--help'"															| tee -a $LOG
  $CRHC --help																																| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - '-h'"																	| tee -a $LOG
  $CRHC -h																																		| tee -a $LOG
}

logout_def()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Logout Pipeline"												| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Logout"																	| tee -a $LOG
  $CRHC logout																																	| tee -a $LOG
}

login_def()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Login Pipeline"	   											| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - login with token"												| tee -a $LOG
  $CRHC login --token $TOKEN																										| tee -a $LOG
}

pytest_def()
{
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Pytest Pipeline"												| tee -a $LOG

  echo "## $(date +%m-%d-%Y_%H:%M:%S) - pytest -v"															| tee -a $LOG
  pytest -v																																			| tee -a $LOG
}




## Main
#
# It starts from here
#


echo "## $(date +%m-%d-%Y_%H:%M:%S) - STARTING"																| tee -a $LOG
if [ ! -f ~/.token ]; then
  echo "Please, create the file '~/.token' with the content as below. Update the token information properly, based on your own token"
  echo "TOKEN=\"eyJhbGciOiJIUzI1NiIsInR5cCIg...\""
  echo "exiting ..."
  exit
fi

check_packages

if [ "$1" == "-h" ] || [ "$1" == "--help" ] || [ "$1" == "" ] ; then
  echo "##########################"
  echo "# crhc-cli End to End Test"
  echo "#-------------------------"
  echo "#"
  echo "# Flags:"
  echo "#   -b <branch_name|optional>"
  echo "#"
  echo "#   -p <pipeline_#|required>"
  echo "#"
  echo "#   -g <git repo|optional>"
  echo "#"
  echo "#"
  echo "# Pipeline Options:"
  echo "#   0 - inventory"
  echo "#   1 - swatch"
  echo "#   2 - patch"
  echo "#   3 - vulnerability"
  echo "#   4 - advisor"
  echo "#   5 - ts"
  echo "#   6 - endpoint"
  echo "#   7 - binary version"
  echo "#   8 - general"
  echo "#   9 - pytest"
  echo "#"
  echo "#   9999 - all together"
  echo "##########################"
  echo ""
  echo "e.g."
  echo ""
  echo "  $ $0 -b fix_report -p 9 -g git@github.com:waldirio/crhc-cli.git"
  echo "  or"
  echo "  $ $0 -b fix_report -p 9 -g https://github.com/waldirio/crhc-cli.git"
  echo "  or"
  echo "  $ $0 -p 9"
fi




# Passing the branch and also the pipeline
if [ "$1" == "-b" ] && [ "$3" == "-p" ] && [ "$5" == "-g" ]; then
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Passing the branch: $2,the pipeline: $4 and the repo: $6"		| tee -a $LOG
  branch=$2
  pipeline=$4
  gitrepo=$6
fi

if [ "$1" == "-p" ]; then
  echo "## $(date +%m-%d-%Y_%H:%M:%S) - Using the origin branch and the pipeline: $2"								| tee -a $LOG
  pipeline=$2
fi

# It only will run once the tester pass the pipeline
if [ $pipeline ]; then
  virtualenv $branch $gitrepo
fi

case $pipeline in
  '0') #echo "inventory"
       logout_def
       inventory_def
       
       login_def
       inventory_def
       ;;
  '1') #echo "swatch"
       logout_def
       swatch_def
       
       login_def
       swatch_def
       ;;
  '2') #echo "patch"
       logout_def
       patch_def
       
       login_def
       patch_def
       ;;
  '3') #echo "vulnerability"
       logout_def
       vulnerability_def
       
       login_def
       vulnerability_def
       ;;
  '4') #echo "advisor"
       logout_def
       advisor_def
       
       login_def
       advisor_def
       ;;
  '5') #echo "ts"
       logout_def
       ts_def
       
       login_def
       ts_def
       ;;
  '6') #echo "ts"
       logout_def
       endpoint_def
       
       login_def
       endpoint_def
       ;;
  '7') #echo "ts"
       logout_def
       binary_def
       
       login_def
       binary_def
       ;;
  '8') #echo "ts"
       logout_def
       general_def
       
       login_def
       general_def
       ;;
  '9') #echo "ts"
       logout_def
       pytest_def

       login_def
       pytest_def
       ;;
  '9999') #echo "all"
       logout_def
       inventory_def
       swatch_def
       patch_def
       vulnerability_def
       advisor_def
       ts_def
       pytest_def

       login_def
       inventory_def
       swatch_def
       patch_def
       vulnerability_def
       advisor_def
       ts_def
       pytest_def
       ;;
  '*') echo "Please, inform a valid pipeline, exiting ...."
     ;;
esac

echo "## $(date +%m-%d-%Y_%H:%M:%S) - ENDING"																	| tee -a $LOG
