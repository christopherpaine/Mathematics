 #!/usr/bin/env bash

 echo "Watching for changes in .py files..."

 while true; do
   # Wait for any .py file to be modified
   inotifywait -e close_write --format '%w%f' *.py | while read FILE; do
     BASENAME="${FILE%.py}"
     NOTEBOOK="${BASENAME}.ipynb"

     if [[ -f "${NOTEBOOK}" ]]; then
       echo "Detected change in ${FILE}"
       echo "Syncing formats for ${NOTEBOOK}..."
       jupytext --sync "${NOTEBOOK}"
       echo "Recalculating notebook ${NOTEBOOK}..."
       jupyter nbconvert --to notebook --inplace --execute --allow-errors "${NOTEBOOK}"
       echo "Rendering HTML for ${NOTEBOOK}..."
       jupyter nbconvert --to html "${NOTEBOOK}" --output "${BASENAME}.html"
       jupyter nbconvert --to html --no-input --no-prompt "${NOTEBOOK}" --output
 "${BASENAME}-clean.html"

       echo "Done processing ${FILE}. Waiting for next change..."
     else
       echo "No corresponding notebook found for ${FILE}. Skipping..."
     fi
   done
 done

