 #!/usr/bin/env bash

 echo "Watching for changes in .py files..."

 # Check if required commands are available
 for cmd in inotifywait jupytext jupyter; do
   if ! command -v $cmd &> /dev/null; then
     echo "Error: $cmd is not installed or not in PATH."
     exit 1
   fi
 done

 while true; do
   # Wait for any .py file to be modified
   inotifywait -e close_write --format '%w%f' *.py | while read FILE; do
     BASENAME="${FILE%.py}"
     NOTEBOOK="${BASENAME}.ipynb"

     if [[ -f "${NOTEBOOK}" ]]; then
       echo "Detected change in ${FILE}"
       echo "Syncing formats for ${NOTEBOOK}..."
       if ! jupytext --sync "${NOTEBOOK}"; then
         echo "Error syncing ${NOTEBOOK}"
         continue
       fi

       echo "Recalculating notebook ${NOTEBOOK}..."
       if ! jupyter nbconvert --to notebook --inplace --execute --allow-errors
 "${NOTEBOOK}"; then
         echo "Error executing ${NOTEBOOK}"
         continue
       fi

       echo "Rendering HTML for ${NOTEBOOK}..."
       if ! jupyter nbconvert --to html "${NOTEBOOK}" --output "${BASENAME}.html"; th
         echo "Error rendering HTML for ${NOTEBOOK}"
         continue
       fi

       if ! jupyter nbconvert --to html --no-input --no-prompt "${NOTEBOOK}" --output
 "${BASENAME}-clean.html"; then
         echo "Error rendering clean HTML for ${NOTEBOOK}"
         continue
       fi

       echo "Done processing ${FILE}. Waiting for next change..."
     else
       echo "No corresponding notebook found for ${FILE}. Skipping..."
     fi
   done
 done


