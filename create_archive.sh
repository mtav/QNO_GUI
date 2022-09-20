#!/bin/bash
git archive --format zip --prefix=QNO_GUI/ --output ../QNO_GUI_$(date +%Y%m%d_%H%M%S).zip main
