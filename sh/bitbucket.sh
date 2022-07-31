#!/usr/local/bin/zsh
CONFIG=".git/config"
if [ -e  $CONFIG ]; then
  FILE=$(<$CONFIG)
  BITBUCKET_HTTPS="https://*@bitbucket.org/*"
  BITBUCKET_GITAT="git@bitbucket.org"
  for line in $FILE
  do
    if [[ $line = $BITBUCKET_HTTPS ]]; then
      open $line
    elif [[ $line = $BITBUCKET_GITAT ]]; then
      open ${line/git@bitbucket.com:/https://bitbucket.com/}
    fi
  done
else
  open "https://bitbucket.org/"
fi
