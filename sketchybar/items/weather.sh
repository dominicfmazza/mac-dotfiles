#!/bin/bash

source "$HOME/.config/sketchybar/colors.sh"

weather=(
  icon.font="$FONT:Bolder:20.0"
  icon.color=$BLACK
  icon.padding_right=0
  icon.y_offset=2
  label.padding_right=0
  label.color=$BLACK
  label.align=right
  label.font="$FONT:Bold:16.0"
  background.drawing=off
  padding_left=0
  padding_right=10
  update_freq=300
  script="$PLUGIN_DIR/weather.sh"
)

sketchybar --add item weather left\
           --set weather "${weather[@]}"
