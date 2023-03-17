#!/bin/bash
source "$HOME/.config/sketchybar/colors.sh" # Loads all defined colors

calendar=(
  icon=cal
  icon.font="$FONT:Mono:16.0"
  icon.padding_right=2
  label.padding_right=0
  label.width=70
  label.align=right
  label.font="$FONT:Bold:16.0"
  background.drawing=off
  padding_left=10
  update_freq=30
  script="$PLUGIN_DIR/calendar.sh"
)

sketchybar --add item calendar right       \
           --set calendar "${calendar[@]}" \
           --subscribe calendar system_woke
