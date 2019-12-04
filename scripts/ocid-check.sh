#!/bin/bash

  REGEX_FOR_OCID="ocid([v]?)1(\.|:)([a-z]*)(\.|:)oc1(\.|:)(iad|phx|)(\.|:)([a-z0-9]*)([(\.|:)([a-z0-9]*)?"
  SAMPLE_OCID_REPLACEMENT_STRING="xxxxxEXAMPLExxxxx"

# Checks if a valid OCID is checked in with the sources
for i in "$@"
do
  if [[ $(stat --printf="%s" "$i") -gt 0 ]]; then # only for non-empty files
    # check if file has any string that matches REGEX for OCID and doesn't have
    # our replacement string
    if grep -E "$REGEX_FOR_OCID" "$i" | grep -E -v "$SAMPLE_OCID_REPLACEMENT_STRING"
    then
      # OCID is found
        OCID_IN_FILE=$(grep -E "$REGEX_FOR_OCID" "$i" | grep -E "$SAMPLE_OCID_REPLACEMENT_STRING")
        >&2 echo "$i has a valid OCID in it. $OCID_IN_FILE"
        exit 1
    fi
  fi
done

# all files passes OCID checks
exit 0

