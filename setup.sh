#!/bin/bash

 # Function to run inside tmux
 run_inside_tmux() {
     echo "Running inside tmux session"
     tmux rename-window bayesian-inference
     echo "just renamed window"
     #set up the panes
     tmux split-window -h
     tmux resize-pane -x 60 
     tmux split-window -v 
#    tmux resize-pane -x "$(($(tmux display -p '#{pane_height}') / 2))"
     tmux split-window -h
     
     tmux send-keys -t 2 "nix-shell" Enter
     tmux send-keys -t 2 "ipython" Enter
     tmux send-keys -t 3 "nix-shell" Enter
     tmux send-keys -t 3 "live-server ." Enter
     tmux send-keys -t 4 "nix-shell" Enter
     tmux send-keys -t 4 "python ./watch.py" Enter
     tmux select-pane -t 1






 }

 # Function to run outside tmux
 run_outside_tmux() {
     echo "Running outside tmux session"
     # Create a new tmux session and run the script inside it
#     tmux new-session -d -s my_session "bash $0 inside"
     tmux new-session -s Bayes-WP
#     tmux attach-session -t my_session
 }

 # Check if running inside tmux
 if [ "$1" == "inside" ]; then
     run_inside_tmux
 else
     run_outside_tmux
 fi








