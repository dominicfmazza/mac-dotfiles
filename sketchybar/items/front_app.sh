#!/bin/bash

FRONT_APP_SCRIPT='sketchybar --set $NAME label="$INFO"'

yabai=(
  script="$PLUGIN_DIR/yabai.sh"
  icon.font="$FONT:Regular:16.0"
  label.drawing=off
  icon.width=30
  icon=$YABAI_GRID
  icon.color=$ORANGE
  associated_display=active
)

front_app=(
  script="$FRONT_APP_SCRIPT"
  icon.drawing=off
  padding_left=0
  label.color=$BLACK
  label.font="$FONT:Regular:16.0"
  associated_display=active
)

sketchybar --add event window_focus            \
           --add event windows_on_spaces       \
           --add item front_app right           \
           --set front_app "${front_app[@]}"   \
           --subscribe front_app front_app_switched \
           --add item yabai right               \
           --set yabai "${yabai[@]}"           \
           --subscribe yabai window_focus      \
                             windows_on_spaces \
                             mouse.clicked     \

