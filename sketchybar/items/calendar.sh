#!/bin/bash

calendar=(
  icon=cal
  icon.font="$FONT:Regular:16.0"
  icon.padding_right=35
  label.width=45
  label.align=right
  label.font="$FONT:Bold:16.0"
  padding_left=15
  update_freq=30
  script="$PLUGIN_DIR/calendar.sh"
  click_script="$PLUGIN_DIR/zen.sh"
)

sketchybar --add item calendar right       \
           --set calendar "${calendar[@]}" \
           --subscribe calendar system_woke
