#!/bin/bash

# Checks if the copyright year is correct for provided files
for i in "$@"
do
  # get year of the last ocmmit
  # YEAR_OF_LAST_COMMIT="$(git log --date=format:%Y --format=%ad "$i"|head -n1)"

  # The above command doesn't work with an older version of git that is
  # installed in OL. So using the hack below to get the year of the
  # last commit
  YEAR_OF_LAST_COMMIT="$(git log --date=iso --format=%ci|cut -d"-" -f1|head -n1)"

  if [[ $(stat --printf="%s" "$i") -gt 0 ]]; then # only for non-empty files
    # get copyright line
    COPYRIGHT_LINE_IN_FILE="$(grep "# Copyright (c)" "$i" | head -n1)"

    if [[ ! -z "$COPYRIGHT_LINE_IN_FILE" ]]; then
      # if the copyright line doesn't have the year of the last commit
      if ! echo "$COPYRIGHT_LINE_IN_FILE" | grep -q "$YEAR_OF_LAST_COMMIT" ; then
        LAST_COMMIT=$(git log --format="%aD %h %s" "$i"|head -n1); >&2 echo "$LAST_COMMIT"
        >&2 echo "$i has invalid an copyright year. It was last updated in $YEAR_OF_LAST_COMMIT, while copyright line says $COPYRIGHT_LINE_IN_FILE"
        exit 1
      fi
    else
      # copyright line is missing
      >&2 echo "$i has copyright line missing"
      exit 1
    fi
  fi
done

# all files passes copyright checks
exit 0

